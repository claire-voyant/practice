-- palin.hs
-- checks if palindrome

main = interact checkPalindrome

checkPalindrome :: String -> String
checkPalindrome contents =
  unlines (map (\xs ->
    if isPalindrome xs then "palindrome" else "not a palindrome")
    (lines contents))
  where isPalindrome xs = xs == reverse xs
