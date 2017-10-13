module Test where

import qualified Data.Set as Set
import qualified Data.Map as Map

infixr 5 :-:
data List a = Empty | a :-: (List a) deriving (Show, Read, Eq, Ord)

infixr 5 .++
(.++) :: List a -> List a -> List a
Empty .++ ys = ys
(x:-:xs) .++ ys = x :-: (xs .++ ys)

data Tree a = EmptyTree | Node a (Tree a) (Tree a) deriving (Show, Read, Eq)
data NewTree a = NewEmptyTree | NewNode {dataPart :: a, leftSubTree :: NewTree a, rightSubTree :: NewTree a} deriving (Show, Read, Eq)

singletonTree :: a -> Tree a
singletonTree x = Node x EmptyTree EmptyTree

newSingletonTree :: a -> NewTree a
newSingletonTree x = NewNode x NewEmptyTree NewEmptyTree

getData :: NewTree a -> a
getData (NewNode a leftSub rightSub) = a

getTreeData :: Tree a -> a
getTreeData (Node a leftSub rightSub) = a

treeInsert :: (Ord a) => a -> Tree a -> Tree a
treeInsert x EmptyTree = singletonTree x
treeInsert x (Node a left right)
  | x == a = Node x left right
  | x <  a = Node a (treeInsert x left) right
  | x >  a = Node a left (treeInsert x right)

treeElem :: (Ord a) => a -> Tree a -> Bool
treeElem x EmptyTree = False
treeElem x (Node a left right)
  | x == a = True
  | x <  a = treeElem x left
  | x >  a = treeElem x right

instance Functor Tree where
  fmap f EmptyTree = EmptyTree
  fmap f (Node x leftSub rightSub) = Node (f x) (fmap f leftSub) (fmap f rightSub)

 

firstSpace :: String -> String
firstSpace = dropWhile (==' ') . dropWhile (/=' ')

tokenize :: String -> (String, String)
tokenize xs = (a,b)
  where a = takeWhile (/=' ') xs
        b = firstSpace xs

sum'' :: (Num a) => [a] -> a
sum'' xs = foldl (\acc x -> acc + x) 0 xs

numLongChains :: Int
numLongChains = length (filter (\xs -> length xs > 15) (map chain [1..100]))

chain :: (Integral a) => a -> [a]
chain 1 = [1]
chain n
  | even n = n:chain(n `div` 2)
  | odd n  = n:chain(n*3+1)

largestDivisible :: (Integral a) => a
largestDivisible = head (filter p [100000,99999..])
  where p x = x `mod` 3829 == 0

filter' :: (a -> Bool) -> [a] -> [a]
filter' _ [] = []
filter' f (x:xs)
  | f x = x : filter' f xs
  | otherwise = filter' f xs

map'' :: (a -> b) -> [a] -> [b]
map'' f xs = foldr (\x acc -> f x : acc) [] xs

map' :: (a -> b) -> [a] -> [b]
map' _ [] = []
map' f (x:xs) = f x : map' f xs

flip' :: (a -> b -> c) -> (b -> a -> c)
flip' f x y = f y x

zipWith' :: (a -> b -> c) -> [a] -> [b] -> [c]
zipWith' _ [] _ = []
zipWith' _ _ [] = []
zipWith' f (x:xs) (y:ys) = f x y : zipWith' f xs ys

multThree :: (Num a) => a -> a
multThree = (*3)

quicksort :: (Eq a, Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) =
  let small = quicksort [a | a <- xs, a <=x]
      big   = quicksort [a | a <- xs, a > x]
  in small ++ [x] ++ big

elem'' :: (Eq a) => a -> [a] -> Bool
elem'' y ys = foldl (\acc x -> if x == y then True else acc) False ys

elem' :: (Eq a) => a -> [a] -> Bool
elem' _ [] = False
elem' e (x:xs)
  | x==e = True
  | otherwise = elem' e xs

zip' :: [a] -> [b] -> [(a,b)]
zip' _ []  = []
zip' [] _  = []
zip' (x:xs) (y:ys) = (x,y):zip' xs ys

repeat' :: (Eq a) => a -> [a]
repeat' x = x:repeat' x

reverse' :: (Eq a) => [a] -> [a]
reverse' (x:xs) = case (x:xs) of
  (x:[]) -> [x]
  _ -> reverse' xs ++ [x]

take' :: (Num i, Ord i) => i -> [a] -> [a]
take' _ [] = []
take' n (x:xs)
  | n <= 0 = []
  | otherwise = x:(take' (n-1) xs)

replicate' :: (Num i, Ord i) => i -> a -> [a]
replicate' n x
  | n <= 0 = []
  | n > 0  = x:replicate' (n-1) x

maxi' :: (Ord a) => [a] -> a
maxi' [] = error "no maximum of empty list"
maxi' [x] = x
maxi' (x:xs)
  | x > maxTail = x
  | otherwise   = maxTail 
  where maxTail = maxi' xs

fib :: (Eq a, Num a) => a -> a
fib 0 = 0
fib 1 = 1
fib x = fib (x-1) + fib (x-2)

combineTriple :: (Num a) => (a,a,a) -> a
combineTriple (x,y,z) = let a=x; b=y; c=z in a+b+c

cylinder :: (RealFloat a) => a -> a -> a
cylinder r h =
  let sideArea = 2 * pi * r * h
      topArea = pi * r ^2
  in sideArea + 2 * topArea

calcBmis :: (RealFloat a) => [(a,a)] -> [a]
calcBmis xs = [bmi w h | (w,h) <- xs]
  where bmi weight height = weight / height ^ 2

initials :: [Char] -> [Char] -> [Char]
initials firstname lastname = [f] ++ ". " ++ [l] ++ "."
  where (f:_) = firstname
        (l:_) = lastname

myCompare :: (Ord a) => a -> a -> Ordering
myCompare a b
  | a > b     = GT
  | a == b    = EQ
  | otherwise = LT

tellMe :: (Integral a, Show a) => a -> [Char]
tellMe something
  | something > 0 = "Greater than Zero."
  | something < 0 = "Less than Zero."
  | otherwise     = "Zero."

sum' :: (Num a) => [a] -> a
sum' [] = 0
sum' (x:xs) = x + sum xs

length' :: (Num b) => [a] -> b
length' [] = 0
length' (x:xs) = 1 + length' xs

head' :: [a] -> a
head' [] = error "Empty list has no head." 
head' (x:_) = x

factorial :: Integral a => a -> a
factorial n = if n == 0 then 1 else n * factorial (n -1)

sayHello :: String -> IO ()
sayHello x = putStrLn ("Hello, " ++ x ++ "!")

myLength :: [z] -> Int
myLength x = length x

trp :: (x,y,z) -> z
trp (x,y,z) = z

myOrder :: (Ord a, Num a) => a -> a -> Ordering
myOrder a b = if a - b >= 0 then GT else LT

doFunc f a = f a

addOne x = 
  x + 1
makeEqual x  y = 
  if (not ( x == y ) && (x < y)) then
    makeEqual (addOne x) y
  else 
    if x < y then 
      "Y is larger!"
    else
      "Equal"

simple y = if (snd y == ()) then fst y else snd y

x = (+)

easyFunction :: Num a => a -> a
easyFunction a = a

myFst :: (a,b) -> a
myFst (a,b) = a

firstOne :: [a] -> a
firstOne (x:xs) = x

myId x = x

-- F :: [Char] -> Integer
legnthPlusOne xd = w `x` 1 
  where w = length xd


--F xs = w + 1
--  where w = length xs

isPalindrome :: (Eq a) => [a] -> Bool
isPalindrome (a:x)
  | (length x) == 0 = True
  | a /= (x !! (length x - 1)) = False
  | a == (x !! (length x - 1)) = isPalindrome (take (length x -1) x)

myAbs :: Integer -> Integer
myAbs x = if x >= 0 then x else (x * (-1))

f :: (a,b) -> (c,d) -> ((b,d) , (a,c))
f (a,b) (c,d) = ((b,d) , (a,c))

cutString :: (Eq n, Num n) => n -> String -> String
cutString n str = case n of
  0 -> tail str 
  n -> cutString (n-1) (tail str)
