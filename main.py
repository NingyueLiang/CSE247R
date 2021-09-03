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

question5()




