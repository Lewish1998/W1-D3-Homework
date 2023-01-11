from src.python_functions_practice import *

import unittest

class TestPythonFunctionPractice(unittest.TestCase):

# done
  def test_return_10(self):
      return_10_result = return_10()
      self.assertEqual( 10, return_10_result )

# done
#   @unittest.skip("delete this line to run the test")
  def test_add(self):
      add_result = add( 1, 2 )
      self.assertEqual( 3, add_result )

# done
  def test_subtract(self):
      subtract_result = subtract( 10, 5 )
      self.assertEqual( 5, subtract_result )

# done
  def test_multiply(self):
      multiply_result = multiply( 4, 2 )
      self.assertEqual( 8, multiply_result )

#  done
  def test_divide(self):
      divide_result = divide( 10, 2 )
      self.assertEqual( 5, divide_result )

# done
  def test_length_of_string(self):
      test_string = "A string of length 21"
      string_length = length_of_string( test_string )
      self.assertEqual( 21, string_length )

# done
  def test_join_string(self):
      string_1 = "Mary had a little lamb, "
      string_2 = "its fleece was white as snow"
      joined_string = join_string( string_1, string_2 )
      self.assertEqual( "Mary had a little lamb, its fleece was white as snow", joined_string )

# done
  def test_add_string_as_number(self):
      add_result = add_string_as_number( "1", "2" )
      self.assertEqual( 3, add_result )

# done
  def test_number_to_full_name__month_1(self):
      result = number_to_full_month_name( 1 )
      self.assertEqual( "January", result )

# done
  def test_number_to_full_name__month_3(self):
      result = number_to_full_month_name( 3 )
      self.assertEqual( "March", result )

# done
  def test_number_to_full_name__month_9(self):
      result = number_to_full_month_name( 9 )
      self.assertEqual( "September", result )

# done
  def test_number_to_short_month_name__month_1(self):
      first_month_string = number_to_short_month_name( 1 )
      self.assertEqual( "Jan", first_month_string )

# done
  def test_number_to_short_month_name__month_4(self):
      fourth_month_string = number_to_short_month_name( 4 )
      self.assertEqual( "Apr", fourth_month_string )

# done
  def test_number_to_short_month_name__month_10(self):
      tenth_month_string = number_to_short_month_name( 10 )
      self.assertEqual( "Oct", tenth_month_string )



  #Further


  #Given the length of a side of a cube calculate the volume
# done
  def test_volume_of_cube(self):
    #add test code here
    volume = cube_volume(13)
    self.assertEqual( 2197, volume ) 

  #Given a String, return the String reversed
# done
  def test_reverse_string(self):
    #add test code here
    result = reverse_string("Please Reverse Me!")
    self.assertEqual( "!eM esreveR esaelP", result ) 


  #Given a value in farenheit, convert this into celsius.
# done
  def test_fahrenheit_to_celsius(self):
    #add test code here
    celsius = convert_to_celcius(50)
    self.assertEqual( 10, celsius ) 



if __name__ == '__main__':
    unittest.main()
