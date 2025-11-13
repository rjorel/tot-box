#!/usr/bin/env hy

(import os)
(import socket)


(def *host* "")
(def *port* 8888)

(def *request-queue-size* 5)


(defn handle-request (connection)
    (do
        (setv request (connection.recv 1024))
        (print (request.decode))

        (connection.sendall (bytes "HTTP/1.1 200 OK\n\nHello world !" "utf-8"))))


(defn handle-connection (sock connection)
    (do
        (setv pid (os.fork))

        (if (= pid 0)
            (do
                (sock.close)
                (handle-request connection)
                (connection.close)
                (os._exit 0))

            (connection.close))))


(defn listen (sock)
    (while True
        (do
            (setv (, connection port) (sock.accept))
            (handle-connection sock connection))))


(defn get-socket ()
    (do
        (setv sock (socket.socket socket.AF_INET socket.SOCK_STREAM))
        (sock.setsockopt socket.SOL_SOCKET socket.SO_REUSEADDR 1)

        (sock.bind (, *host* *port*))
        (sock.listen *request-queue-size*))
    sock)


(defmain [&rest _]
    (do
        (setv sock (get-socket))
        (print (.format "Serving HTTP on port {0} .." *port*))
        (listen sock)))