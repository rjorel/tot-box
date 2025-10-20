;; Random histogram
(defun create-hist (n)
 (make-array n :initial-element 0))

(defun add-value-hist (hist n)
 (incf (aref hist n)))

(defun create-random-hist (m n)
 (let ((hist (create-hist n)))
  (dotimes (i m)
   (add-value-hist hist (random n)))
  hist))

(defun print-hist (hist &key (output *standard-output*))
 (let ((n (length hist)))
  (dotimes (i n)
   (format output "~A [~A] ~A ~%" i
    (aref hist i)
    (make-string (aref hist i) :initial-element #\*)))))


;; Storage in file.
(defparameter *flow* (open "histogram" :direction :output :if-exists :supersede))
(defparameter *hist* (create-random-hist 20 5))
(print-hist *hist* :output *flow*)

(close *flow*)