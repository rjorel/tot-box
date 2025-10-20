(defun partition (pred l)
 (labels ((partition-aux (pred l res1 res2)
           (if (endp l)
            (values res1 res2)
            (if (funcall pred (car l))
             (partition-aux pred (cdr l) (append res1 (list (car l))) res2)
             (partition-aux pred (cdr l) res1 (append res2 (list (car l))))))))

  (partition-aux pred l '() '())))

(defun quick-sort (less-than l)
 (cond
  ((endp l) '())
  ((endp (cdr l)) l)
  (t (multiple-value-bind (l-inf l-sup)
      (partition (lambda (x) (funcall less-than x (car l))) (cdr l))
      (append (quick-sort less-than l-inf)
       (list (car l))
       (quick-sort less-than l-sup))))))


(describe
  (quick-sort #'< '(5 7 2 1 9 4.2 -5 -10 0)))