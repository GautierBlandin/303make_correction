import parsing


def test_parse_file():
    parsed = parsing.parse_file(parsing.read_file("example"))

    assert parsed["tty"].name == "tty"
    assert parsed["tty"].dep_type == "rule"
    assert parsed["tty"].dependencies == ["fc.o", "tty.o"]
    assert parsed["tty"].command == "cc -o tty tty.o fc.o"

    assert parsed["fc.o"].name == "fc.o"
    assert parsed["fc.o"].dep_type == "rule"
    assert parsed["fc.o"].dependencies == ["fc.c", "fc.h"]
    assert parsed["fc.o"].command == "cc -c fc.c"

    assert parsed["fc.c"].name == "fc.c"
    assert parsed["fc.c"].dep_type == "file"
    assert parsed["fc.c"].dependencies is None
    assert parsed["fc.c"].command is None
