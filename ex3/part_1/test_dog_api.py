import pytest
from src.api import Api


@pytest.fixture(scope='function')
def pet_api_user():
    return Api("https://dog.ceo/api")


expected_body_of_breeds = {
    "message": {
        "affenpinscher": [],
        "african": [],
        "airedale": [],
        "akita": [],
        "appenzeller": [],
        "australian": [
            "shepherd"
        ],
        "basenji": [],
        "beagle": [],
        "bluetick": [],
        "borzoi": [],
        "bouvier": [],
        "boxer": [],
        "brabancon": [],
        "briard": [],
        "buhund": [
            "norwegian"
        ],
        "bulldog": [
            "boston",
            "english",
            "french"
        ],
        "bullterrier": [
            "staffordshire"
        ],
        "cattledog": [
            "australian"
        ],
        "chihuahua": [],
        "chow": [],
        "clumber": [],
        "cockapoo": [],
        "collie": [
            "border"
        ],
        "coonhound": [],
        "corgi": [
            "cardigan"
        ],
        "cotondetulear": [],
        "dachshund": [],
        "dalmatian": [],
        "dane": [
            "great"
        ],
        "deerhound": [
            "scottish"
        ],
        "dhole": [],
        "dingo": [],
        "doberman": [],
        "elkhound": [
            "norwegian"
        ],
        "entlebucher": [],
        "eskimo": [],
        "finnish": [
            "lapphund"
        ],
        "frise": [
            "bichon"
        ],
        "germanshepherd": [],
        "greyhound": [
            "italian"
        ],
        "groenendael": [],
        "havanese": [],
        "hound": [
            "afghan",
            "basset",
            "blood",
            "english",
            "ibizan",
            "plott",
            "walker"
        ],
        "husky": [],
        "keeshond": [],
        "kelpie": [],
        "komondor": [],
        "kuvasz": [],
        "labradoodle": [],
        "labrador": [],
        "leonberg": [],
        "lhasa": [],
        "malamute": [],
        "malinois": [],
        "maltese": [],
        "mastiff": [
            "bull",
            "english",
            "tibetan"
        ],
        "mexicanhairless": [],
        "mix": [],
        "mountain": [
            "bernese",
            "swiss"
        ],
        "newfoundland": [],
        "otterhound": [],
        "ovcharka": [
            "caucasian"
        ],
        "papillon": [],
        "pekinese": [],
        "pembroke": [],
        "pinscher": [
            "miniature"
        ],
        "pitbull": [],
        "pointer": [
            "german",
            "germanlonghair"
        ],
        "pomeranian": [],
        "poodle": [
            "medium",
            "miniature",
            "standard",
            "toy"
        ],
        "pug": [],
        "puggle": [],
        "pyrenees": [],
        "redbone": [],
        "retriever": [
            "chesapeake",
            "curly",
            "flatcoated",
            "golden"
        ],
        "ridgeback": [
            "rhodesian"
        ],
        "rottweiler": [],
        "saluki": [],
        "samoyed": [],
        "schipperke": [],
        "schnauzer": [
            "giant",
            "miniature"
        ],
        "segugio": [
            "italian"
        ],
        "setter": [
            "english",
            "gordon",
            "irish"
        ],
        "sharpei": [],
        "sheepdog": [
            "english",
            "shetland"
        ],
        "shiba": [],
        "shihtzu": [],
        "spaniel": [
            "blenheim",
            "brittany",
            "cocker",
            "irish",
            "japanese",
            "sussex",
            "welsh"
        ],
        "spitz": [
            "japanese"
        ],
        "springer": [
            "english"
        ],
        "stbernard": [],
        "terrier": [
            "american",
            "australian",
            "bedlington",
            "border",
            "cairn",
            "dandie",
            "fox",
            "irish",
            "kerryblue",
            "lakeland",
            "norfolk",
            "norwich",
            "patterdale",
            "russell",
            "scottish",
            "sealyham",
            "silky",
            "tibetan",
            "toy",
            "welsh",
            "westhighland",
            "wheaten",
            "yorkshire"
        ],
        "tervuren": [],
        "vizsla": [],
        "waterdog": [
            "spanish"
        ],
        "weimaraner": [],
        "whippet": [],
        "wolfhound": [
            "irish"
        ]
    },
    "status": "success"
}

expected_body_of_sub_breeds = {
    "message": [
        "afghan",
        "basset",
        "blood",
        "english",
        "ibizan",
        "plott",
        "walker"
    ],
    "status": "success"
}


@pytest.mark.parametrize("breed", ["breed/african", "breed/doberman", "breed/affenpinscher"])
def test_get_dog_by_breed(pet_api_user, breed):
    dog_response = pet_api_user.get_data(breed, 'images/random')
    assert dog_response.status_code == 200


def test_get_list_of_breeds(pet_api_user):
    dog_list_response = pet_api_user.get_data("breeds", "list/all").json()
    for key, value in expected_body_of_breeds.items():
        assert dog_list_response[key] == value, (
            f'[{key}] Actual value: {dog_list_response[key]}, expected: {value}'
        )


def test_get_random_image(pet_api_user):
    random_image_response = pet_api_user.get_data("breeds", "image/random")
    assert random_image_response.status_code == 200

# Non-parametrized test
def test_get_list_of_sub_breeds(pet_api_user):
    dog_list_response = pet_api_user.get_data("breed", "hound/list").json()
    for key, value in expected_body_of_sub_breeds.items():
        assert dog_list_response[key] == value, (
            f'[{key}] Actual value: {dog_list_response[key]}, expected: {value}'
        )


# Parametrized test
@pytest.mark.parametrize("breed,expected_result", [("hound", {'message': ['afghan', 'basset', 'blood', 'english',
                                                                          'ibizan', 'plott', 'walker'],
                                                              'status': 'success'}),
                                                   ("mastiff", {'message': ['bull', 'english', 'tibetan'],
                                                                'status': 'success'}),
                                                   ("terrier", {'message': ['american', 'australian', 'bedlington',
                                                                            'border', 'cairn', 'dandie', 'fox', 'irish',
                                                                            'kerryblue', 'lakeland', 'norfolk',
                                                                            'norwich', 'patterdale', 'russell',
                                                                            'scottish', 'sealyham', 'silky', 'tibetan',
                                                                            'toy', 'welsh', 'westhighland', 'wheaten',
                                                                            'yorkshire'],
                                                                'status': 'success'})])
def test_get_list_of_sub_breeds_parametrized(pet_api_user, breed, expected_result):
    dog_list_response = pet_api_user.get_data("breed", breed+"/list").json()
    for key, value in expected_result.items():
        assert dog_list_response[key] == value, (
            f'[{key}] Actual value: {dog_list_response[key]}, expected: {value}'
        )
