import System.IO

main = do
  line <- getLine
  ineof <- hIsEOF line
  if ineof 
    then return ()
    else do
      putStrLn $ reverseWords line
      main

reverseWords :: String -> String
reverseWords = unwords . map reverse .words
