# Open Sublime text editor, create a new Python file, copy the following code in it and save it as 'census_app.py'.

# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


@st.cache()
def load_data():
	# Load the Adult Income dataset into DataFrame.

	df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)
	df.head()

	# Rename the column names in the DataFrame. 

	# Create the list
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race', 'gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	# Rename the columns using 'rename()'
	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)

	# Print the first five rows of the DataFrame
	df.head()

	# Replace the invalid values ' ?' with 'np.nan'.

	df = df.replace(' ?',np.nan)


	# Delete the rows with invalid values and the column not required 

	# Delete the rows with the 'dropna()' function
	df.dropna(inplace=True)

	# Delete the column with the 'drop()' function
	df.drop(columns='fnlwgt',axis=1,inplace=True)

	return df

census_df = load_data()

st.title("the census project")
# Write the code to design the web app
if st.sidebar.checkbox("show raw data"):
  st.subheader("Census Data Set")
  st.dataframe(census_df)


# Write your code to filter streamlit warnings 
st.set_option('deprecation.showPyplotGlobalUse', False)



# Write the code to design the web app

# Add title on the main page and in the sidebar.

# Add a multiselect widget to allow the user to select multiple visualisations.
# Add a subheader in the sidebar with the label "Visualisation Selector"
st.sidebar.subheader("Visualisation Selector")

# Add a multiselect in the sidebar with label 'Select the Charts/Plots:'
# Store the current value of this widget in a variable 'plot_list'.
plots = st.sidebar.multiselect("select the plots",("pie plot","boxplot","count plot"))

# Display pie plot using matplotlib module and 'st.pyplot()'

if "pie plot" in plots:
  pie_feats = st.sidebar.multiselect("select the features for pie plot",census_df.columns)
  for i in pie_feats:
    st.subheader(f"distrubution of records for different {i}")
    pie_data = census_df[i].value_counts()
    plt.pie(pie_data,labels = set(census_df[i].unique()),explode = [0,0.15])
    st.pyplot()

# Display box plot using matplotlib module and 'st.pyplot()'
if "boxplot" in plots:
  box_feats = st.sidebar.multiselect("select the features for box plot",census_df.columns)
  for i in box_feats:
    st.subheader(f"distrubution of records for different {i}")
    sns.boxplot(y = i,x ='hours-per-week',data = census_df)
    st.pyplot()

# Display count plot using seaborn module and 'st.pyplot()' 
if 'count plot' in plots:
    st.subheader("Count plot")
    plt.figure(figsize = (10,7))
    sns.countplot('workclass',data = census_df)
    st.pyplot()
