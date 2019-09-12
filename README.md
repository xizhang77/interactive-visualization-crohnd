# interactive-visualization-crohnd

In this repo, a interactive visualization framework for a correlation-based analysis is introduced. The data used here is issued from a study of the adverse events of a drug on 117 patients affected by Crohn’s disease. The tool allows users to see the relationships between each feature.


## Structure of the folder

Here is the structure of the whole repo

```
README.md
/mysite
    app.py
    /input
        the dataset (.csv)
    /templates
        index.html
    /static
        /css
        ...
```

* The Flask server's code is stored under app.py
* The custom CSS codes are stored under /static/css
* All the charts and front-end code can be found in /templates/index.html

## Charts in framework
Here are totally 4 charts in the visualization framework:

* The correlogram shows the correlations between each features
* The scatter plot shows the embedded features in 2D space, which also indicate the correlations (if two features are close to each other, then they are high correlated)
* Age segment bar chart shows the distribution of patients by ages
* Detail view in Parallel Coordinate for all the data in the datasets

### Parallel Coordinate 

Parallel coordinates is a common way of visualizing and analyzing the multivariate data. One data in n-dimensional space is represented as a polyline with vertices on the parallel axes and the position of the vertex on the i-th axis corresponds to the i-th coordinate of the point.


## How to run the code

* Download the dataset (CrohnD.csv) from [R Datasets](https://github.com/vincentarelbundock/Rdatasets/blob/master/csv/robustbase/CrohnD.csv) and save the CSV file in the /input folder.
* From the /mysite folder, run _python app.py_

After the server initializes it will listen on port 5000 waiting for connections. Now open up the web browser and enter the following URL in the address field:

http://localhost:5000

Now you can play on the visualization tool!

