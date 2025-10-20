;; Color definition
(defclass color ()
 ((r :initarg :r :reader red-of)
  (g :initarg :g :reader green-of)
  (b :initarg :b :reader blue-of)))

;; Color methods
(defmethod print-object ((c color) stream)
 (format stream "color{red: ~d, green: ~d, blue: ~d}"
  (red-of c)
  (green-of c)
  (blue-of c)))

(defmethod warm-colorp ((c color))
 (< (blue-of c)
  (red-of c)))

(defun make-color (&key (r 0) (g 0) (b 0))
 (make-instance 'color :r r :g g :b b))

(defun keylist (table)
 (let ((l '()))
  (maphash (lambda (key val)
            (declare (ignore val))
            (push key l))
   table)
  l))

(defun extract-warm-color (colors)
 (let ((l '()))
  (with-hash-table-iterator (entry colors)
   (loop (multiple-value-bind (more name color) (entry)
          (unless more (return l))
          (when (warm-colorp color)
           (push name l)))))))


;; Hash creation
(defparameter *colors* (make-hash-table))

;; Entries adding
(setf (gethash 'red *colors*) (make-color :r 255))
(setf (gethash 'green *colors*) (make-color :g 255)) 
(setf (gethash 'blue *colors*) (make-color :b 255)) 

;; Entries suppression
(remhash 'blue *colors*)

;; Little summary
(describe *colors*)