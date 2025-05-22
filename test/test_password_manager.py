import pytest
from unittest.mock import patch
from utils.get_user_input import get_user_input
from utils.exit import check_exit

exit
class TestGetUserInput:
    @pytest.mark.it("should accept valid inputs of 'e', 'r', 'd', 'l' and 'x'")
    @patch('utils.get_user_input.input')
    def test_get_user_input_returns_valid_inputs(self, mock_input):
        mock_input.return_value = 'e'
        assert get_user_input() == 'e'
        mock_input.return_value = 'r'
        assert get_user_input() == 'r'
        mock_input.return_value = 'd'
        assert get_user_input() == 'd'
        mock_input.return_value = 'l'
        assert get_user_input() == 'l'
        mock_input.return_value = 'x'
        assert get_user_input() == 'x'
        
    @patch('utils.get_user_input.input')
    @pytest.mark.it("should return valid letters in lowercase")
    def test_get_user_input_returns_valid_capitals_in_lower_case(self, mock_input):
        mock_input.return_value = 'E'
        assert get_user_input() == 'e'
        
    @patch('utils.get_user_input.input')
    @pytest.mark.it("should return zero if input invalid")
    def test_get_user_input_return_zero_for_invalid_input(self, mock_input):
        mock_input.return_value = 'p'
        assert get_user_input() == 0
        mock_input.return_value = '3'
        assert get_user_input() == 0
        mock_input.return_value = '?'
        assert get_user_input() == 0
        
class TestExit:
    @pytest.mark.it("should return false if user input is not 'x'")
    def test_exit_returns_false_if_input_not_x(self):
        test_input = 'l'
        assert check_exit(test_input) is False
    @pytest.mark.it("should return true if user input is 'x'")
    def test_exit_returns_true_if_input_is_x(self):
        test_input = 'x'
        assert check_exit(test_input) is True

         
        
    
    
    
        
        