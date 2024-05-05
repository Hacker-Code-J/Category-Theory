f1 :: Int -> (Int, String)
f1 x = (x + 1, show x ++ "+1")

f2 :: Int -> (Int, String)
f2 x = (x + 2, show x ++ "+2")

f3 :: Int -> (Int, String)
f3 x = (x + 3, show x ++ "+3")

unit :: Int -> (Int, String)
unit x = (x, "Ops:")

bind :: (Int, String) -> (Int -> (Int, String)) -> (Int, String)
bind t f =
  let (res, log) = f (fst t)
      combinedLog = snd t ++ log ++ ";"
  in (res, combinedLog)

-- Direct calls setup
directCalls :: (Int, String)
directCalls =
  let x = 0
      (res1, log1) = f1 x
      (res2, log2) = f2 res1
      (res3, log3) = f3 res2
      finalLog = "Ops:" ++ log1 ++ log2 ++ log3 ++ ";"
  in (res3, finalLog)

-- Functional approach setup
functionalApproach :: (Int, String)
functionalApproach =
  let x = 0
      result = bind (bind (bind (unit x) f1) f2) f3
  in result
