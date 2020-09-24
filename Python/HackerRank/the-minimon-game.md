https://www.hackerrank.com/challenges/the-minion-game/problem

```python
def minion_game(s):
    stuart_score=0
    kevin_score=0
    vowels="AEIOU"
    for i in range(len(s)):
        if s[i] in vowels:
            kevin_score=kevin_score+len(s)-i
        else:
            stuart_score=stuart_score+len(s)-i
    if kevin_score>stuart_score:
        print("Kevin "+str(kevin_score))
    elif kevin_score<stuart_score:
        print("Stuart "+str(stuart_score)) 
    else:
        print("Draw")                  

    

if __name__ == '__main__':
    s = input()
    minion_game(s)


```
