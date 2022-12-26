import textwrap

def wrap(string, max_width):
    '''
    wrap the string into a paragraph of width  max_width
    '''
    wrapper = textwrap.TextWrapper(max_width) 
    wrapped_string = wrapper.fill(string)
    
    return wrapped_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)