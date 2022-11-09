from statistics import stdev
import unittest
import pandas as pd

from src.serie_numeric.logics import NumericColumn

class TestSerieNumeric(unittest.TestCase):
    # set up mock column called inte
    def setUp(self) -> None:
        self.nc = NumericColumn( 'postgres','student', 'inte')
        self.nc.serie = pd.DataFrame({'inte': [-1,-4,7,50,7,7,7,7,7,7]})
        self.nc.set_data()
        return super().setUp()
    
    def test_numeric_column_exist(self):
        self.assertTrue(self.nc)
        
    def test_unique_values(self):
        df = self.nc.get_summary_df()
        mask = df['Description'] == 'Number of Unique Values'
        self.assertEqual( int(df[mask].Values.item()), 4 )
        
    def test_missing_value_rows(self):
        df = self.nc.get_summary_df()
        mask = df['Description'] == 'Number of Rows with Missing Values'
        self.assertEqual( int(df[mask]['Values'].item()), 0 )
    
    def test_zero_value_rows(self):
        df = self.nc.get_summary_df()
        mask = df['Description'] == 'Number of Rows with 0'
        self.assertEqual( int(df[mask]['Values'].item()), 0 )
    
    def test_negative_value_rows(self):
        df = self.nc.get_summary_df()
        mask = df['Description'] == 'Number of Rows with Negative Values'
        self.assertEqual( int(df[mask]['Values'].item()), 2 )
    
    def test_average_value(self):
        df = self.nc.get_summary_df()
        mask = df['Description'] == 'Average Value'
        self.assertAlmostEqual( float(df[mask]['Values'].item()), (-1-4+7+50+7+7+7+7+7+7) / 10 )
    
    def test_std_value(self):
        df = self.nc.get_summary_df()
        mask = df['Description'] == 'Standard Deviation Value'        
        self.assertAlmostEqual( float(df[mask]['Values'].item()), stdev([-1,-4,7,50,7,7,7,7,7,7]) )
    
    def test_min_value(self):
        df = self.nc.get_summary_df()
        mask = df['Description'] == 'Minimum Value'
        self.assertAlmostEqual( float(df[mask]['Values'].item()), -4 )
    
    def test_max_value(self):
        df = self.nc.get_summary_df()
        mask = df['Description'] == 'Maximum Value'
        self.assertAlmostEqual( float(df[mask]['Values'].item()), 50 )
    
    def test_median_value(self):
        df = self.nc.get_summary_df()
        mask = df['Description'] == 'Median Value'
        self.assertAlmostEqual( float(df[mask]['Values'].item()), 7 )
    
    def test_freq_df(self):
        self.nc.serie = pd.DataFrame({'inte': [-1,-4,7,50,7,7,7,7,7,7]})
        self.nc.set_frequent()
        self.assertTrue(self.nc.frequent.equals(pd.DataFrame({'value':[7,-4,-1,50],
                                                                'occurrence':[7,1,1,1],
                                                                'percentage':[0.7,0.1,0.1,0.1]
                                                                                        })))
    
    def test_histogram(self):
        self.nc.serie = pd.DataFrame({'inte': [-1,-4,7,50,7,7,7,7,7,7]})
        self.nc.set_histogram()
        self.assertTrue(self.nc.histogram)



if __name__ == '__main__':
    unittest.main(verbosity=2)