#lang racket
(define oneCount 0)
(define zeroCount 0)

(define p (lambda (x)
  (set! oneCount (index-of x 0))
  (if (> (length x) 0)
      (set! zeroCount (- (length x) oneCount))
      (set! oneCount #f))
  (eq? oneCount zeroCount)))


    