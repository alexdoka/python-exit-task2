import logging
import unittest

from tagscounteralexdoka import tagcounter


class TestCalc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("tagscounteralexdoka/synonims.yaml", "a") as file_object:
            file_object.write("\ntricky: supertrickysite.com\n")

    @classmethod
    def tearDownClass(cls):
        def delete_last_strings(filename, number_last_lines):
            fd = open(filename, "r")
            d = fd.read()
            fd.close()
            m = d.split("\n")
            s = "\n".join(m[:-int(number_last_lines)])
            fd = open(filename, "w")
            for i in range(len(s)):
                fd.write(s[i])
            fd.close()

        delete_last_strings("tagscounteralexdoka/synonims.yaml", 2)
        delete_last_strings("tagscounteralexdoka/tags_log_file", 2)

    def test_get_url_site(self):
        self.assertEqual(tagcounter.get_url_site('google.com'), 'https://google.com/')

    def test_define_site_name(self):
        self.assertEqual(tagcounter.define_site_name('tricky', file="tagscounteralexdoka/synonims.yaml"),
                         'supertrickysite.com')
        self.assertEqual(tagcounter.define_site_name('megasite.com', file="tagscounteralexdoka/synonims.yaml"),
                         'megasite.com')

    def test_get_dict_tags(self):
        self.assertEqual(tagcounter.get_dict_tags('<html><a><a><a test="string"><body>'),
                         {'html': 1, 'a': 3, 'body': 1})

    def test_write_to_logfile(self):
        logging.basicConfig(filename="/home/doka/learn/python/exit_task_7/tagscounteralexdoka/tags_log_file",
                            level=logging.INFO,
                            format='%(asctime)s:%(message)s')

        tagcounter.write_to_logfile("supertest")
        result = False
        with open('/home/doka/learn/python/exit_task_7/tagscounteralexdoka/tags_log_file', 'r') as file_object:
            for ln in file_object:
                if "supertest" in ln:
                    print(ln)
                    result = True
                    break
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
