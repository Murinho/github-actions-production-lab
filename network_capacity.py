def aws_usable_ipv4_addresses(prefix_length: int) -> int:
    """
    Return the number of usable IPv4 addresses in an AWS subnet.

    AWS reserves five IPv4 addresses per subnet.
    For this lab, restrict ourselves to normal AWS IPv4 subnet
    prefix sizes /16 through /28.
    """
    if not 16 <= prefix_length <= 28:
        raise ValueError("prefix_length must be between /16 and /28")

    total_addresses = 1 << (32 - prefix_length)
    return total_addresses - 5