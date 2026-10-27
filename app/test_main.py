from unittest import mock
import pytest


from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_url_valid, internet_connection, result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
    is_url_valid: bool,
    internet_connection: bool,
    result: str,
    mock_valid_url: mock.MagicMock,
    mock_has_internet_connection: mock.MagicMock
) -> None:
    mock_valid_url.return_value = is_url_valid
    mock_has_internet_connection.return_value = internet_connection

    assert (
        can_access_google_page("https://google.com") == result
    )
