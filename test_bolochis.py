from bolochis_validator import BolochisParser


def probar_casos():
    valid_cases = [
        "int:age=22",
        'string:greeting="Hola"',
        "fn greeting() : { int:x=1 }",
        "assuming age >= 18 : { bool:mayor=true } otherwise : { bool:mayor=false }",
        "loop (age < 30) : { int:step=1 }",
    ]

    invalid_cases = [
        "int:age=abc",
        "fn () : { }",
        "assuming age > 10 { int:a=1 }",  # falta ':'
    ]

    for code in valid_cases:
        parser = BolochisParser(code)
        assert parser.analize(), f"It should be valid: {code} -> {parser.error}"

    for code in invalid_cases:
        parser = BolochisParser(code)
        assert not parser.analize(), f"It should have failed: {code}"

    print("All test cases passed.")


if __name__ == "__main__":
    probar_casos()