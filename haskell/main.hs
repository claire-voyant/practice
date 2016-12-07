main = do
  contents <- readFile "./main.hs"
  return (lines contents)
