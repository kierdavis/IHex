import unittest
from ihex import IHex


class IHexTest(unittest.TestCase):
    def test_row_bytes(self):
        ihex = IHex()
        self.assertEqual(ihex.write(), ':00000001FF\r\n')
        ihex.insert_data(6,
                'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuwvxyz')
        self.assertEqual(ihex.write(),
                ':100006004142434445464748494A4B4C4D4E4F5062\r\n' \
                ':100016005152535455565758595A30313233343554\r\n' \
                ':10002600363738396162636465666768696A6B6C1E\r\n' \
                ':0E0036006D6E6F707172737475777678797A6B\r\n' \
                ':00000001FF\r\n')
        ihex.set_row_bytes(8)
        self.assertEqual(ihex.write(),
                ':080006004142434445464748CE\r\n' \
                ':08000E00494A4B4C4D4E4F5086\r\n' \
                ':0800160051525354555657583E\r\n' \
                ':08001E00595A303132333435F8\r\n' \
                ':0800260036373839616263646A\r\n' \
                ':08002E0065666768696A6B6C86\r\n' \
                ':080036006D6E6F70717273743E\r\n' \
                ':06003E0075777678797AEF\r\n' \
                ':00000001FF\r\n')
        ihex.set_row_bytes(32)
        self.assertEqual(ihex.write(),
                ':200006004142434445464748494A4B4C4D4E4F505152535455565758595A303132333435CC\r\n' \
                ':1E002600363738396162636465666768696A6B6C6D6E6F707172737475777678797ABF\r\n' \
                ':00000001FF\r\n')

# TODO: add tests for
# read(str)
# read_file(file_name)
# set_start(start_addr)
# set_mode(8/16/32)
# get_area(addr)
# insert_data(addr, data)
# calc_checksum(hexstr)
# parse_line(ihex_line)
# write()
# write_file(file_name)

if __name__ == '__main__':
    unittest.main()
