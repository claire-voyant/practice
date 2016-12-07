-- contents.hs
-- gets contents of a file
-- puts them back out in caps

import Data.Char

main = do
  contents <- getContents
  putStr (map toUpper contents)
