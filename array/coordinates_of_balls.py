# // Example input: "1.0,2.1,3.2,4.3,5.4,6.5,7.6,8.7,9.8\n2.1,3.2,4.3,5.4,6.5,7.6,8.7,9.8,10.9\n3.2,4.3,5.4,6.5,7.6,8.7,9.8,10.9,11.1"
#
#
#
def find_closest_ball(str):
  tokens = str.split('\n')
  min_dist = 9999999999999
  ball = 0
  counter = 0
  for t in tokens:
    counter += 1
    cordinates = t.split(',')
    sum = 0
    for index in range(len(cordinates)):
      sum += (float(cordinates[index]) * float(cordinates[index]))
    if (math.sqrt(sum) < min_dist):
      min_dist = math.sqrt(sum)
      ball = counter
  return min_dist, ball


min_dist, ball = find_closest_ball('1.0,2.1,3.2,4.3,5.4,6.5,7.6,8.7,9.8\n2.1,3.2,4.3,5.4,6.5,7.6,8.7,9.8,10.9\n3.2,4.3,5.4,6.5,7.6,8.7,9.8,10.9,11.1')
print(min_dist)
print(ball)
