#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from flask import Flask, render_template
import json

from sklearn import manifold, preprocessing

def ageSegment( num ):
  # Getting the age segment for visualization
  if num <= 30:
    return '30-'
  elif num <= 40:
    return '31-40'
  elif num <= 50:
    return '41-50'
  elif num <= 55:
    return '51-55'
  elif num <= 60:
    return '56-60'
  else:
    return '60+'

def MDS( df ):
  # Getting the 2D cooridinates for attributes using MDS

  new_df = df.drop( columns = 'age_segment' )
  coef = 1 - new_df.corr()
  
  mds = manifold.MDS(n_components=2, max_iter=3000, dissimilarity="precomputed")
  pos = mds.fit(coef).embedding_

  column_name = list(df.columns.values)

  mds_data = pd.DataFrame( columns = ['x', 'y', 'attr'] ) 

  for i in range(len(pos)):
    mds_data.loc[i, 'x'] = pos[i][0]
    mds_data.loc[i, 'y'] = pos[i][1]
    mds_data.loc[i, 'attr'] = column_name[i]

  return mds_data


app = Flask(__name__)

@app.route("/")
@app.route("/data")

def index():
  df = pd.read_csv('input/CrohnD.csv', index_col = 0)
  df = df.drop(columns='ID')
  
  # Converting categorical data into numeric
  df['country'] = df['country'].astype('category')
  df['sex'] = df['sex'].astype('category')
  df['treat'] = df['treat'].astype('category')

  cat_cols = df.select_dtypes(['category']).columns
  df[cat_cols] = df[cat_cols].apply( lambda x: x.cat.codes )


  # Generating the age segment
  df['age_segment'] = df['age'].apply( lambda age: ageSegment(age) )


  pc_data = df.to_json( orient= 'records' )
  corr_data = df.corr().to_json( orient='index' )
  mds_data = MDS( df ).to_json( orient= 'records' )

  return render_template("index.html",
    pc_data = pc_data,
    mds_data = mds_data,
    corr_data = corr_data )

if __name__ == "__main__":
    app.run( host='0.0.0.0', port=5000, debug=True )

