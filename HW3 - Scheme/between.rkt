#lang racket
(define (between I J K)
  (cond
    ((and (< I K) (> J K)) #t)
    ((and (< J K) (> I K)) #t)
    (else #f)))


  