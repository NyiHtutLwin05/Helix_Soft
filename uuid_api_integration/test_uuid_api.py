
import pytest
from unittest.mock import Mock, patch
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from helixsoft_avalon import UUIDGenerator

# //
class TestUUIDGenerator:
    """Simple tests for UUID API"""
    
    def test_api_works(self):
        """Test API returns UUID when working"""
        generator = UUIDGenerator()

        with patch('helixsoft_avalon.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.text = '["test-uuid-1234"]'
            mock_get.return_value = mock_response
            
            uuid = generator.get_uuid()
            assert uuid == "test-uuid-1234"
    
    def test_api_fails_uses_fallback(self):
        """Test when API fails, uses local UUID"""
        generator = UUIDGenerator()

        with patch('helixsoft_avalon.requests.get') as mock_get:
            mock_get.side_effect = Exception("API down")
            
            uuid = generator.get_uuid()
            assert uuid is not None
            assert len(uuid) > 10
    
    def test_uuid_format(self):
        """Test UUID format looks right"""
        generator = UUIDGenerator()
        
        with patch('helixsoft_avalon.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.text = '["550e8400-e29b-41d4-a716-446655440000"]'
            mock_get.return_value = mock_response
            
            uuid = generator.get_uuid()
            assert len(uuid) == 36
            assert uuid.count('-') == 4