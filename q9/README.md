You are given N recipes, the K-th of which is represented by a string A[K]. Each letter of the string represents a single unit of an ingredient: for example, recipe "toast" requires two units of ingredient 't' and one unit of ingredients 'o', 'a' and 's'.
You are also given a list of available ingredients represented by a string S. Which recipes can be prepared using ingredients from the list?
Write a function:
def solution(A, S)
that, given an array A consisting of N strings representing the recipes, and a string S representing the list of available ingredients, returns the number of recipes that can be prepared using available ingredients.
Examples:
1. Given A = ["toast", "bread", "breada", "cheese"] and S = "abcdeeehrs", the function should return 2. With our ingredients, recipes "bread" and "cheese" can be prepared (note that it is not necessary to create both at the same time). We cannot prepare "toast" as some ingredients are missing (for example 't'), and there are not enough units of 'a' to prepare "breada".
2. Given A = ["az", "azz", "zza", "zzz", "zzzz"] and S = "azzz", the function should return 4. With our ingredients, we can prepare "az", "azz", "zza" and "zzz".
