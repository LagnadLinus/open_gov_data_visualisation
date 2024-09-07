

import matplotlib.pyplot as plt
import io
import base64



def generate_visualization(data, plot_type='histogram'):
    # Create a new figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))  # Figure size can be adjusted based on preference
    
    # Check the type of plot we want to generate
    if plot_type == 'histogram':
        # Example: Histogram for family income distribution
        ax.hist(data['income'], bins=20, color='skyblue', edgecolor='black')
        ax.set_title('Distribution of Family Income', fontsize=14)
        ax.set_xlabel('Income', fontsize=12)
        ax.set_ylabel('Number of Families', fontsize=12)
        
    elif plot_type == 'bar':
        # Example: Bar chart for education levels
        education_counts = data['education_level'].value_counts()
        ax.bar(education_counts.index, education_counts.values, color='green')
        ax.set_title('Education Level Distribution', fontsize=14)
        ax.set_xlabel('Education Level', fontsize=12)
        ax.set_ylabel('Count', fontsize=12)
    
    elif plot_type == 'line':
        # Example: Line chart for income over years
        ax.plot(data['year'], data['income'], color='purple')
        ax.set_title('Family Income over Years', fontsize=14)
        ax.set_xlabel('Year', fontsize=12)
        ax.set_ylabel('Income', fontsize=12)

    # Save the plot to a BytesIO object in memory
    buf = io.BytesIO()  # Buffer to hold the image
    plt.savefig(buf, format='png')  # Save the plot as a PNG image in the buffer
    buf.seek(0)  # Move the pointer to the beginning of the buffer
    
    # Close the figure to free memory
    plt.close(fig)
    
    # Encode the image in base64 so it can be rendered in an HTML img tag
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    
    # Return the base64-encoded image data
    return img_base64
