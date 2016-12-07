-- reverse.hs

module Reverse where

rvrs :: String -> String
rvrs x = (drop 9 x) ++ " " ++ [(x !! 6)] ++ [(x !! 7)] ++" " ++(take 5 x)


main :: IO ()
main = print (rvrs "Curry is awesome!")
