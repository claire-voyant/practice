-- read.hs
-- read a file

import System.IO

main = do
  withFile "song.txt" ReadMode (\handle -> do
    contents <- hGetContents handle
    putStr contents)
