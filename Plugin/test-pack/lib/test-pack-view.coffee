module.exports =
class TestPackView

  constructor: (serializedState) ->
    # Create root element
    @element = document.createElement('div')
    @element.classList.add('test-pack')

  getElement: ->
    @element

  log: (output) ->
    #SOURCE:: https://gist.github.com/frane/1542526
    #SOURCE:: https://coffeescript-cookbook.github.io/chapters/strings/splitting-a-string
    output = output.split "\n" #split the output into an array based on new line characters
    for item in output  #for each line in the array we can create a new div to conatin it
      newMessage = document.createElement('div')
      newMessage.textContent = item
      newMessage.classList.add('message')
      @element.appendChild(newMessage)
