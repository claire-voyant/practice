main :: IO ()
main = do
  contents <- getContents
  putStrLn contents
  let myLines = lines contents
  mapM putStrLn myLines
  mainloop myLines
  return ()

mainloop :: [String] -> IO ()  
mainloop contents@(x:xs) = do 
  words x
  mapM putStrLn words
  if xs == [] then
    return ()
  else
    mainloop xs
    


