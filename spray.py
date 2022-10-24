import json

class spray():
    def __init__(self, pseudo) -> None:
        self.separators = ['', '.', '-', '_']
        self.pseudo = pseudo

    class Person:
        def __init__(self, line):
            line = line.strip() # remove surrounding whitespace
            
            if not line:
                raise Exception("Empty input for person. Empty line?")

            name_list = line.split(" ")
            self.firstname = name_list[0]
            self.lastname = None

            if len(name_list) > 1:
                self.lastname = name_list[1]
        
        def to_dict(self):
            return { 'firstname': self.firstname, 'lastname': self.lastname }
        
        def to_json(self):
            return json.dumps(self.to_dict())

        def __str__(self):
            return self.to_json()

    def single_name(self, name):
        if not name:
            return []
        result = set()
        name = name.strip()

        # mixed case
        result.add(name)
        result.add(name.lower().capitalize())
        # lowercase
        result.add(name.lower())
        # uppercase
        result.add(name.upper())
        
        return result

    def combine_names(self, firstname, lastname):
        if not firstname or not lastname:
            return []

        result = set()
        # mixed case
        for sep in self.separators:
            # unchanged
            result.add(firstname + sep + lastname)
            result.add(firstname[0] + sep + lastname)
            result.add(lastname + sep + firstname)
            result.add(lastname[0] + sep + firstname)
            # capitalized
            result.add(firstname.lower().capitalize() + sep + lastname.lower().capitalize())
            result.add(firstname[0].lower().capitalize() + sep + lastname.lower().capitalize())
            result.add(lastname.lower().capitalize() + sep + firstname.lower().capitalize())
            result.add(lastname[0].lower().capitalize() + sep + firstname.lower().capitalize())
            # lowercase
            result.add(firstname.lower() + sep + lastname.lower())
            result.add(firstname[0].lower() + sep + lastname.lower())
            result.add(lastname.lower() + sep + firstname.lower())
            result.add(lastname[0].lower() + sep + firstname.lower())
            # uppercase
            result.add(firstname.upper() + sep + lastname.upper())
            result.add(firstname[0].upper() + sep + lastname.upper())
            result.add(lastname.upper() + sep + firstname.upper())
            result.add(lastname[0].upper() + sep + firstname.upper())

        return result

    def run(self):    
        people = []

        try:
            p = self.Person(self.pseudo)
            people.append(p)
        except Exception as e:
            pass

        results = set()

        for p in people:
            fp = self.single_name(p.firstname)
            sp = self.single_name(p.lastname)
            cb = self.combine_names(p.firstname, p.lastname)
            results.update(fp)
            results.update(sp)
            results.update(cb)

        return sorted(results)
