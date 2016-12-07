-- colors.hs
-- asks for your color-number order
-- then reapeats them

import Control.Monad
main = do
  colors <- forM [1,2,3,4] (\a -> do
    putStr $ "Which color do youa sociate with the number "
    putStrLn $  show a ++ "?"
    color <- getLine
    return color)
  putStrLn "The colors you associate with 1,2,3,4 are: " 
  mapM_ putStrLn colors

    
