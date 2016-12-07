-- caps.hs
-- takes any input and makes its caps

import Control.Monad
import Data.Char

main = forever $ do
  putStr "Input please: "
  l <- getLine
  putStrLn $ map toUpper l
