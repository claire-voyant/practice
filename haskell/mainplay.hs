-- messing with returns

main = do
  return ()
  return "ahahaa"
  line <- getLine
  return 4
  return line
  putStrLn line
