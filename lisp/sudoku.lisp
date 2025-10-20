;; Display a well-formatted grid.
(defun grid-display (grid)
 (format *standard-output* "   | A  B  C | D  E  F | G  H  I |~%")
 (dotimes (i 9)
  (when (= (mod i 3) 0)                                               ; A line of '*' is put every 3 lines.
   (format *standard-output* "**********************************~%"))

  (format *standard-output* " ~a " (1+ i))
  (dotimes (j 9)
   (when (= (mod j 3) 0)                                             ; A '|' is put every 3 columns.
    (format *standard-output* "|"))
   (format *standard-output* " ~a " (if (= (aref grid i j) 0)        ; Don't display 0 values.
                                     " "
                                     (aref grid i j))))

  (format *standard-output* "|~%"))
 (format *standard-output* "**********************************~%"))     ; Last line.


;; Test functions.
(defun grid-inline-p (line value grid)
 (dotimes (i 9)
  (when (= (aref grid line i) value)
   (return t))))

(defun grid-incolumn-p (col value grid)
 (dotimes (i 9)
  (when (= (aref grid i col) value)
   (return t))))

(defun grid-inblock-p (line column value grid)
 ; Compute cases for current block.
 (let ((bline (- line (mod line 3)))      
       (bcol  (- column (mod column 3))))

  (dotimes (i 9)
   (when (= (aref grid (+ bline (floor i 3)) (+ bcol (mod i 3))) value)
    (return t)))))

;; Availability test.
(defun grid-check-p (line column value grid)
 (or (grid-inline-p line value grid)
  (grid-incolumn-p column value grid)
  (grid-inblock-p line column value grid)))


(defun grid-put (line column value grid)
 (let* ((table '(("A" . 0) ("B" . 1) ("C" . 2)
                 ("D" . 3) ("E" . 4) ("F" . 5)
                 ("G" . 6) ("H" . 7) ("I" . 8)))
        (col (assoc column table :test #'string-equal)))

  ; Error tests.. users can be stupid sometimes !
  (when (null col)
   (error "This column doesn't exist"))

  (when (or (< line 1) (> line 9))
   (error "This line doesn't exist"))

  (unless (= (aref grid (1- line) (cdr col)) 0)
   (error "This case is already taken"))

  (if (grid-check-p (1- line) (cdr col) value grid)
   (format *standard-output* "This place is not available.~%")
   (setf (aref grid (1- line) (cdr col)) value))))


(defun sudoku (grid)
 (assert (equal (array-dimensions grid) '(9 9)) ()
  "Bad dimensions (must be 9x9)")

 (let ((line ())
       (column ())
       (value ()))

  (loop 
   (grid-display grid)
   (princ "Case (column, line): ")
   (setf column (read))
   (setf line (read))

   (princ "Value: ")
   (setf value (read))
   (grid-put line column value grid))))


(defparameter *grid* (make-array '(9 9) :initial-contents                ; Test grid.
                      '((1 0 0 0 0 4 0 0 5)
                          (0 0 0 9 5 0 0 8 0)
                          (0 0 0 0 0 3 0 9 0)
                          (0 0 5 0 0 2 0 0 4)
                          (0 0 1 0 6 0 7 0 0)
                          (7 0 0 3 0 0 2 0 0)
                          (0 6 0 5 0 0 0 0 0)
                          (0 8 0 0 1 6 0 0 0)
                          (5 0 0 2 0 0 0 0 7))))


(sudoku *grid*)