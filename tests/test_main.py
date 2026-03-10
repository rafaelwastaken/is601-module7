import pytest
from pathlib import Path
from unittest.mock import patch
from main import is_valid_url, create_directory, generate_qr_code


def test_is_valid_url_accepts_valid_http():
    assert is_valid_url("http://example.com") is True


def test_is_valid_url_accepts_valid_https():
    assert is_valid_url("https://github.com/rafaelwastaken") is True


def test_is_valid_url_rejects_plain_string():
    assert is_valid_url("not-a-url") is False


def test_is_valid_url_rejects_empty_string():
    assert is_valid_url("") is False


def test_create_directory_creates_new_dir(tmp_path):
    new_dir = tmp_path / "test_dir"
    create_directory(new_dir)
    assert new_dir.exists() and new_dir.is_dir()


def test_create_directory_existing_dir(tmp_path):
    # Should not raise when directory already exists
    create_directory(tmp_path)
    assert tmp_path.exists()


def test_generate_qr_code_creates_file(tmp_path):
    output_path = tmp_path / "test_qr.png"
    generate_qr_code("https://example.com", output_path)
    assert output_path.exists()
    assert output_path.stat().st_size > 0


def test_generate_qr_code_custom_colors(tmp_path):
    output_path = tmp_path / "test_qr_colors.png"
    generate_qr_code("https://example.com", output_path, fill_color="blue", back_color="yellow")
    assert output_path.exists()
    assert output_path.stat().st_size > 0


def test_generate_qr_code_invalid_url(tmp_path):
    output_path = tmp_path / "should_not_exist.png"
    generate_qr_code("not-a-url", output_path)
    assert not output_path.exists()
