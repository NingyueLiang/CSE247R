def question1():
  array = [1, 2, 3, 4, 5, 5, 6]
  target = 11
  length = len(array)
  print(length)
  for i in range(length):
    for j in range(i+1, length):
      if array[i] + array[j] == target:
        print('Indices: {x}, {y}'.format(x = i, y = j))
        x_ans = array[i]
        y_ans = array[j]

        #PSEUDOCODE: search array for x_ans and y_ans
        return((i, j))

#question1()

def question2():
  word = 'kayak'
  palin = list(word)
  print(palin)
  rev_palin = palin[::-1]
  print(rev_palin)
  if palin ==rev_palin:
    return True
  else:
    return False


  #PSEUDOCODE:
    #divide array by half(remove character in the middle if odd length)
    #check if both halves are equal
#print(question2())


def helper(word):
  return word[::-1]

def question3():
  sentence = 'I have a dog.'
  new_sentence = ''
  test = sentence.split()
  print(test)
  for word in test:
    new_sentence = new_sentence+helper(word)+' '
  print(new_sentence)

##question3()

def question4():
  sentence = 'I have have a a dog dog.'
  new_sentence = ''
  test = sentence.split()
  wl =set()
  for word in test:
    if word in wl:
      new_sentence = new_sentence+'Y'+' '
    else:
      wl.add(word)
      new_sentence = new_sentence+'N'+' '
  print(new_sentence)

def question5():
  array1 = [0,1,2,3]
  array2 = [0,3,6,78,99]

  arraymerge = array1+array2
  arraymerge.sort()
  print(arraymerge)

#question5()




