-- serach.hs
-- search over a list containing tuples to find closest
-- TODO:: extend to n-tuples

module TupleSearch where

import Data.List

data ClassMapList a = Empty | Cons ((a,a),a) (ClassMapList ((a,a),a)) deriving (Show, Read, Eq, Ord)


createClassMap :: (a,a) -> a -> ClassMapList a
createClassMap (x,y) label = Cons ((x,y), label) Empty

euclideanDistance :: (Num a, Floating a) => (a,a) -> (a,a) -> a
euclideanDistance (x,y) (a,b) =
  let squaredDiffA = (x-a)*(x-a)
      squaredDiffB = (y-b)*(y-b)
  in sqrt(squaredDiffA + squaredDiffB)

euclideanOfEach :: (Num b, Floating a, Enum b) => [(a,a)] -> (a,a) -> [(a,b)]
euclideanOfEach xs (a,b) = zip (map (euclideanDistance (a,b)) xs) [0..]

findClosestTuple :: (Ord a, Floating a) => [(a,a)] -> (a,a) -> (a,a)
findClosestTuple xs (x,y) = xs !! (snd ((sort (euclideanOfEach (xs) (x,y))) !! 0))
  
  
  
  
   


