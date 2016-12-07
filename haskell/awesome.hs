-- awesome.hs

module Awesome where

addBang input = input ++ "!"

takeFour input = (!!) input 4

dropNine input = drop 9 input

returnThirdChar :: String -> Char
returnThirdChar input = (!!) input 2

myString :: String
myString = "Curry is awesome!"
letterIndex :: Int -> Char
letterIndex index = (!!) myString index

rvrs = (drop 9 myString) ++ " " ++ [(myString !! 6)] ++ [(myString !! 7)] ++" " ++(take 5 myString)
