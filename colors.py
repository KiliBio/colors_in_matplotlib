import matplotlib.pyplot as plt
import matplotlib.lines as lines
import matplotlib.cm as cm

##### Technique 1: For the use in an iterative way! like for-loop  

### Method 1: Generate a costum color gradient situated in between two "extreme" colors 
# Checkout a color picker online such as: https://www.w3schools.com/colors/default.asp

# for example blues  
blues = generate_gradient("#5D8AFF","#9BC3FF", len(X))

def generate_gradient(start_color, end_color, n):
    # Convert the start and end colors to RGB values
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))

    # Calculate the color increment for each RGB channel
    r_step = (end_rgb[0] - start_rgb[0]) / (n - 1)
    g_step = (end_rgb[1] - start_rgb[1]) / (n - 1)
    b_step = (end_rgb[2] - start_rgb[2]) / (n - 1)

    # Generate the gradient list of colors
    gradient = []
    for i in range(n):
        r = int(start_rgb[0] + i * r_step)
        g = int(start_rgb[1] + i * g_step)
        b = int(start_rgb[2] + i * b_step)
        hex_color = f"#{r:02X}{g:02X}{b:02X}"
        gradient.append(hex_color)
    return gradient


### Method 2: Get n numbers of different colors from a pre-defined color-list
# See: https://matplotlib.org/stable/gallery/color/colormap_reference.html
     
# for example the "rainbow" collection
def get_colors(number):
    color_list = cm.get_cmap('rainbow', number)
    return color_list


##### Technique 2: Indirectly determine the colors used:

# First define your color palette: 

dist_colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4',
          '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff',
          '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1',
          '#000075', '#808080']

rainbow = ['#e71d43', '#ff0000', '#ff3700', '#ff6e00', '#ffa500', '#ffc300',
           '#ffe100', '#ffff00', '#aad500', '#55aa00', '#008000', '#005555',
           '#002baa', '#0000ff', '#1900d5', '#3200ac', '#4b0082', '#812ba6',
           '#b857ca', '#d03a87']

# Tell python to use a certain color palette   
ax.set_prop_cycle(color=rainbow)

# Python automatically cycles though the colors 
ax.plot(x, y, label=names)
 