import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, scrolledtext
import random
import json
import os
import base64

# ==============================================================================
# SECTION 1: THE MATHEMATICAL VAULT (100 HARDCODED FUNCTIONS)
# ==============================================================================
# This class contains 100 unique, reversible mathematical functions.
# Each function maps (x, y, z) -> Integer using bitwise packing and unique constants.
# They are hardcoded as requested.
# ==============================================================================

class MathVault:
    def __init__(self):
        # We store pairs of (Forward Function, Inverse Function)
        # To keep the code "Hardcoded" and explicit, we define the logic map below.
        # Format: Index: (Encryption_Lambda, Decryption_Lambda)
        # Logic: Packed = (x<<16 + y<<8 + z). Result = (Packed ^ KEY) + OFFSET
        
        self.functions = {
            0: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x1A2B3C) + 1001, lambda r: ((r - 1001) ^ 0x1A2B3C)),
            1: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x998877) + 2505, lambda r: ((r - 2505) ^ 0x998877)),
            2: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xAA11BB) + 3141, lambda r: ((r - 3141) ^ 0xAA11BB)),
            3: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xCCDD22) + 9921, lambda r: ((r - 9921) ^ 0xCCDD22)),
            4: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x123456) + 7777, lambda r: ((r - 7777) ^ 0x123456)),
            5: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x654321) + 8888, lambda r: ((r - 8888) ^ 0x654321)),
            6: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xF0F0F0) + 1212, lambda r: ((r - 1212) ^ 0xF0F0F0)),
            7: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x0F0F0F) + 3434, lambda r: ((r - 3434) ^ 0x0F0F0F)),
            8: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xBEEF99) + 5656, lambda r: ((r - 5656) ^ 0xBEEF99)),
            9: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xDEAD00) + 7878, lambda r: ((r - 7878) ^ 0xDEAD00)),
            10: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xCAFE01) + 1111, lambda r: ((r - 1111) ^ 0xCAFE01)),
            11: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x8BADF0) + 2222, lambda r: ((r - 2222) ^ 0x8BADF0)),
            12: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x0D15EA) + 3333, lambda r: ((r - 3333) ^ 0x0D15EA)),
            13: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x15EA5E) + 4444, lambda r: ((r - 4444) ^ 0x15EA5E)),
            14: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xA5E515) + 5555, lambda r: ((r - 5555) ^ 0xA5E515)),
            15: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x00FF00) + 6666, lambda r: ((r - 6666) ^ 0x00FF00)),
            16: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xFF00FF) + 9090, lambda r: ((r - 9090) ^ 0xFF00FF)),
            17: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xABCDEF) + 1357, lambda r: ((r - 1357) ^ 0xABCDEF)),
            18: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xFEDCBA) + 2468, lambda r: ((r - 2468) ^ 0xFEDCBA)),
            19: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x13579B) + 1029, lambda r: ((r - 1029) ^ 0x13579B)),
            20: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x2468AC) + 3847, lambda r: ((r - 3847) ^ 0x2468AC)),
            21: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x993311) + 4756, lambda r: ((r - 4756) ^ 0x993311)),
            22: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x113399) + 5867, lambda r: ((r - 5867) ^ 0x113399)),
            23: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x7722EE) + 6978, lambda r: ((r - 6978) ^ 0x7722EE)),
            24: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xEE2277) + 1002, lambda r: ((r - 1002) ^ 0xEE2277)),
            25: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x445566) + 2003, lambda r: ((r - 2003) ^ 0x445566)),
            26: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x665544) + 3004, lambda r: ((r - 3004) ^ 0x665544)),
            27: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x998800) + 4005, lambda r: ((r - 4005) ^ 0x998800)),
            28: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x008899) + 5006, lambda r: ((r - 5006) ^ 0x008899)),
            29: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xAAAAAA) + 6007, lambda r: ((r - 6007) ^ 0xAAAAAA)),
            30: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xBBBBBB) + 7008, lambda r: ((r - 7008) ^ 0xBBBBBB)),
            31: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xCCCCCC) + 8009, lambda r: ((r - 8009) ^ 0xCCCCCC)),
            32: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xDDDDDD) + 9010, lambda r: ((r - 9010) ^ 0xDDDDDD)),
            33: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xEEEEEE) + 1122, lambda r: ((r - 1122) ^ 0xEEEEEE)),
            34: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x121212) + 2233, lambda r: ((r - 2233) ^ 0x121212)),
            35: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x232323) + 3344, lambda r: ((r - 3344) ^ 0x232323)),
            36: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x343434) + 4455, lambda r: ((r - 4455) ^ 0x343434)),
            37: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x454545) + 5566, lambda r: ((r - 5566) ^ 0x454545)),
            38: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x565656) + 6677, lambda r: ((r - 6677) ^ 0x565656)),
            39: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x676767) + 7788, lambda r: ((r - 7788) ^ 0x676767)),
            40: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x787878) + 8899, lambda r: ((r - 8899) ^ 0x787878)),
            41: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x898989) + 9900, lambda r: ((r - 9900) ^ 0x898989)),
            42: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x909090) + 1010, lambda r: ((r - 1010) ^ 0x909090)),
            43: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x090909) + 2020, lambda r: ((r - 2020) ^ 0x090909)),
            44: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xABABAB) + 3030, lambda r: ((r - 3030) ^ 0xABABAB)),
            45: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xBABABA) + 4040, lambda r: ((r - 4040) ^ 0xBABABA)),
            46: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xCDCDCD) + 5050, lambda r: ((r - 5050) ^ 0xCDCDCD)),
            47: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xDCDCDC) + 6060, lambda r: ((r - 6060) ^ 0xDCDCDC)),
            48: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xEFEFEF) + 7070, lambda r: ((r - 7070) ^ 0xEFEFEF)),
            49: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xFEFEFE) + 8080, lambda r: ((r - 8080) ^ 0xFEFEFE)),
            50: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xA0A0A0) + 9091, lambda r: ((r - 9091) ^ 0xA0A0A0)),
            51: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x0B0B0B) + 1234, lambda r: ((r - 1234) ^ 0x0B0B0B)),
            52: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x1C1C1C) + 4321, lambda r: ((r - 4321) ^ 0x1C1C1C)),
            53: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x2D2D2D) + 5678, lambda r: ((r - 5678) ^ 0x2D2D2D)),
            54: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x3E3E3E) + 8765, lambda r: ((r - 8765) ^ 0x3E3E3E)),
            55: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x4F4F4F) + 1350, lambda r: ((r - 1350) ^ 0x4F4F4F)),
            56: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x505050) + 2460, lambda r: ((r - 2460) ^ 0x505050)),
            57: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x616161) + 3570, lambda r: ((r - 3570) ^ 0x616161)),
            58: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x727272) + 4680, lambda r: ((r - 4680) ^ 0x727272)),
            59: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x838383) + 5790, lambda r: ((r - 5790) ^ 0x838383)),
            60: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x949494) + 6801, lambda r: ((r - 6801) ^ 0x949494)),
            61: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xA5A5A5) + 7912, lambda r: ((r - 7912) ^ 0xA5A5A5)),
            62: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xB6B6B6) + 8023, lambda r: ((r - 8023) ^ 0xB6B6B6)),
            63: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xC7C7C7) + 9134, lambda r: ((r - 9134) ^ 0xC7C7C7)),
            64: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xD8D8D8) + 1245, lambda r: ((r - 1245) ^ 0xD8D8D8)),
            65: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xE9E9E9) + 2356, lambda r: ((r - 2356) ^ 0xE9E9E9)),
            66: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xFAFAFA) + 3467, lambda r: ((r - 3467) ^ 0xFAFAFA)),
            67: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x1B2C3D) + 4578, lambda r: ((r - 4578) ^ 0x1B2C3D)),
            68: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x4E5F60) + 5689, lambda r: ((r - 5689) ^ 0x4E5F60)),
            69: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x718293) + 6790, lambda r: ((r - 6790) ^ 0x718293)),
            70: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xA4B5C6) + 7801, lambda r: ((r - 7801) ^ 0xA4B5C6)),
            71: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xD7E8F9) + 8912, lambda r: ((r - 8912) ^ 0xD7E8F9)),
            72: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x0C1D2E) + 9023, lambda r: ((r - 9023) ^ 0x0C1D2E)),
            73: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x3F4051) + 1133, lambda r: ((r - 1133) ^ 0x3F4051)),
            74: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x627384) + 2244, lambda r: ((r - 2244) ^ 0x627384)),
            75: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x95A6B7) + 3355, lambda r: ((r - 3355) ^ 0x95A6B7)),
            76: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xC8D9EA) + 4466, lambda r: ((r - 4466) ^ 0xC8D9EA)),
            77: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xFBF001) + 5577, lambda r: ((r - 5577) ^ 0xFBF001)),
            78: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x2E3142) + 6688, lambda r: ((r - 6688) ^ 0x2E3142)),
            79: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x516273) + 7799, lambda r: ((r - 7799) ^ 0x516273)),
            80: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x8493A4) + 8800, lambda r: ((r - 8800) ^ 0x8493A4)),
            81: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xB7C4D5) + 9911, lambda r: ((r - 9911) ^ 0xB7C4D5)),
            82: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xEAF506) + 1022, lambda r: ((r - 1022) ^ 0xEAF506)),
            83: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x1D2637) + 2133, lambda r: ((r - 2133) ^ 0x1D2637)),
            84: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x405768) + 3244, lambda r: ((r - 3244) ^ 0x405768)),
            85: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x738899) + 4355, lambda r: ((r - 4355) ^ 0x738899)),
            86: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xA6B9CA) + 5466, lambda r: ((r - 5466) ^ 0xA6B9CA)),
            87: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xD9EAFB) + 6577, lambda r: ((r - 6577) ^ 0xD9EAFB)),
            88: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x0C1F22) + 7688, lambda r: ((r - 7688) ^ 0x0C1F22)),
            89: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x3F4253) + 8799, lambda r: ((r - 8799) ^ 0x3F4253)),
            90: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x627384) + 9800, lambda r: ((r - 9800) ^ 0x627384)),
            91: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x95A4B5) + 1591, lambda r: ((r - 1591) ^ 0x95A4B5)),
            92: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xC8D5E6) + 2602, lambda r: ((r - 2602) ^ 0xC8D5E6)),
            93: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xFB0617) + 3713, lambda r: ((r - 3713) ^ 0xFB0617)),
            94: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x2E3748) + 4824, lambda r: ((r - 4824) ^ 0x2E3748)),
            95: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x516879) + 5935, lambda r: ((r - 5935) ^ 0x516879)),
            96: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x8499AA) + 6046, lambda r: ((r - 6046) ^ 0x8499AA)),
            97: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xB7CCDB) + 7157, lambda r: ((r - 7157) ^ 0xB7CCDB)),
            98: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0xEAFDEC) + 8268, lambda r: ((r - 8268) ^ 0xEAFDEC)),
            99: (lambda x, y, z: (((x << 16) | (y << 8) | z) ^ 0x1D2EFD) + 9379, lambda r: ((r - 9379) ^ 0x1D2EFD)),
        }

    def get_forward(self, index):
        return self.functions[index][0]

    def get_inverse(self, index):
        return self.functions[index][1]

# ==============================================================================
# SECTION 2: ENCRYPTION ENGINE LOGIC
# ==============================================================================

class EncryptionEngine:
    def __init__(self):
        self.vault = MathVault()
        # LOREM text for padding
        self.lorem_junk = "LOREM_IPSUM_DOLOR_SIT_AMET_CONSECTETUR_ADIPISCING_ELIT_SED_DO_EIUSMOD_TEMPOR_INCIDIDUNT_UT_LABORE_ET_DOLORE_MAGNA_ALIQUA_UT_ENIM_AD_MINIM_VENIAM_QUIS_NOSTRUD_EXERCITATION_ULLAMCO_LABORIS_NISI_UT_ALIQUIP_EX_EA_COMMODO_CONSEQUAT"

    def _pad_ascii_list(self, ascii_list):
        """
        Ensures the list length is divisible by 3 by appending LOREM text.
        """
        remainder = len(ascii_list) % 3
        if remainder != 0:
            needed = 3 - remainder
            # Detect LOREM logic: We assume the LOREM text is constant junk.
            # We take the first 'needed' characters from the constant.
            junk_ascii = [ord(c) for c in self.lorem_junk[:needed]]
            ascii_list.extend(junk_ascii)
        return ascii_list

    def _remove_padding(self, text):
        """
        Checks if the text ends with the start of the LOREM text and removes it.
        """
        # We need to be careful. The user might type LOREM. 
        # But per instructions: "automatically detects... and removes".
        # We check for suffix match of length 1 or 2 (since max padding is 2).
        # Length 1 check
        if text.endswith(self.lorem_junk[:1]):
            # Check if it was 2
            if text.endswith(self.lorem_junk[:2]):
                return text[:-2]
            return text[:-1]
        return text

    def generate_shuffled_indices(self):
        """Generates a list of 0-99 in random order."""
        indices = list(range(100))
        random.shuffle(indices)
        return indices

    def encrypt_layer(self, input_data_string, indices_key):
        """
        Performs one layer of encryption using the specific indices_key.
        input_data_string: The string to encrypt.
        Returns: A list of encrypted integers.
        """
        # 1. Convert to ASCII
        ascii_vals = [ord(c) for c in input_data_string]
        
        # 2. Pad
        ascii_vals = self._pad_ascii_list(ascii_vals)
        
        encrypted_values = []
        
        # 3. Process in chunks of 3 (x, y, z)
        # We cycle through the 100 functions using the shuffled indices.
        num_triplets = len(ascii_vals) // 3
        
        for i in range(num_triplets):
            x = ascii_vals[i*3]
            y = ascii_vals[i*3 + 1]
            z = ascii_vals[i*3 + 2]
            
            # Use modulo to wrap around the shuffled 100 functions if input is long
            func_idx_ptr = i % 100 
            real_func_idx = indices_key[func_idx_ptr]
            
            # Get function and calculate
            func = self.vault.get_forward(real_func_idx)
            result = func(x, y, z)
            encrypted_values.append(result)
            
        return encrypted_values

    def decrypt_layer(self, encrypted_integers, indices_key):
        """
        Performs one layer of decryption.
        Returns: The decrypted string.
        """
        decrypted_chars = []
        
        for i, val in enumerate(encrypted_integers):
            # Determine which function was used
            func_idx_ptr = i % 100
            real_func_idx = indices_key[func_idx_ptr]
            
            # Get inverse function
            inv_func = self.vault.get_inverse(real_func_idx)
            
            # Reverse the math to get packed int
            packed_res = inv_func(val)
            
            # Unpack x, y, z (Reversing: (x<<16) | (y<<8) | z)
            z = packed_res & 0xFF
            y = (packed_res >> 8) & 0xFF
            x = (packed_res >> 16) & 0xFF
            
            decrypted_chars.extend([chr(x), chr(y), chr(z)])
            
        full_text = "".join(decrypted_chars)
        return self._remove_padding(full_text)

    def perform_redundant_encryption(self, text, rounds):
        """
        Handles the 2X-10X logic.
        Returns: (Final Encrypted String, Master Key List)
        Master Key List Format: [[idx_round1], [idx_round2], ..., "r=N"]
        """
        current_text = text
        master_key = []
        
        for r in range(rounds):
            # Generate new key for this round
            key_indices = self.generate_shuffled_indices()
            master_key.append(key_indices)
            
            # Encrypt
            encrypted_ints = self.encrypt_layer(current_text, key_indices)
            
            # Convert ints to a string representation for the next layer (or final output)
            # We use JSON dump of the list -> Base64 to keep it "text friendly" for the next round's ASCII conversion
            json_str = json.dumps(encrypted_ints)
            b64_bytes = base64.b64encode(json_str.encode('utf-8'))
            current_text = b64_bytes.decode('utf-8')
            
        # Add redundancy flag
        if rounds > 1:
            master_key.append(f"r={rounds}")
        else:
            # Even if 1 round (standard), we keep structure consistent or handle differently.
            # Prompt implies standard is just keys. But for consistency in this function:
            pass 

        return current_text, master_key

    def perform_redundant_decryption(self, encrypted_text, master_key):
        """
        Handles decryption based on key structure.
        """
        # Check for redundancy flag
        rounds = 1
        if isinstance(master_key[-1], str) and master_key[-1].startswith("r="):
            rounds = int(master_key[-1].split("=")[1])
            keys_to_use = master_key[:-1]
        else:
            # Standard single encryption, key might be just a list of ints [0...99] (flat)
            # OR a list of lists [[0...99]]. We need to handle both.
            if isinstance(master_key[0], list):
                keys_to_use = master_key
                rounds = len(master_key)
            else:
                # Flat list
                keys_to_use = [master_key]
                rounds = 1
        
        # Decrypt in reverse order (Outer layer first -> Inner layer)
        # However, our encryption loop: Layer 1 (Text->Enc), Layer 2 (Enc->Enc2)...
        # So EncryptedText is Layer N. We must decrypt Layer N using Key N, then N-1...
        
        current_text = encrypted_text
        
        # Iterate backwards through keys
        for i in range(rounds - 1, -1, -1):
            key = keys_to_use[i]
            
            # Current text is Base64 encoded JSON of ints (from the previous encryption step)
            try:
                b64_bytes = base64.b64decode(current_text)
                json_str = b64_bytes.decode('utf-8')
                encrypted_ints = json.loads(json_str)
            except Exception as e:
                # If this fails, it might be the raw file content if user messed up, 
                # but we assume valid integrity based on prompt.
                raise ValueError("Corrupt file format or wrong key depth.")

            current_text = self.decrypt_layer(encrypted_ints, key)
            
        return current_text

# ==============================================================================
# SECTION 3: GUI & APPLICATION LOGIC
# ==============================================================================

class TotalNotepadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TOTAL NOTEPAD - Custom Encryption Tool")
        self.root.geometry("800x600")
        
        self.engine = EncryptionEngine()
        self.last_used_key = None # Stores key in memory
        self.redundancy_level = 1 # Default 1X
        
        # --- UI Setup ---
        
        # Menu
        menubar = tk.Menu(root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open Encrypted File", command=self.open_file)
        file_menu.add_command(label="Save as Encrypted", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        tools_menu = tk.Menu(menubar, tearoff=0)
        tools_menu.add_command(label="Special Redundant Encryption", command=self.open_redundancy_window)
        tools_menu.add_command(label="Key Manager", command=self.open_key_manager)
        menubar.add_cascade(label="Tools", menu=tools_menu)
        
        root.config(menu=menubar)
        
        # Text Area
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Consolas", 12))
        self.text_area.pack(expand=True, fill='both')
        
        # Status Bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready. Encryption Level: 1X")
        status_bar = tk.Label(root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def open_redundancy_window(self):
        win = tk.Toplevel(self.root)
        win.title("Redundant Encryption Settings")
        win.geometry("300x200")
        
        lbl = tk.Label(win, text="Select Encryption Depth (2X - 10X):")
        lbl.pack(pady=10)
        
        scale = tk.Scale(win, from_=2, to=10, orient=tk.HORIZONTAL)
        scale.set(max(2, self.redundancy_level)) # Set to current or min 2
        scale.pack(pady=10)
        
        def apply():
            self.redundancy_level = scale.get()
            self.status_var.set(f"Ready. Encryption Level: {self.redundancy_level}X")
            messagebox.showinfo("Applied", f"Encryption set to {self.redundancy_level}X.\nKeys will be longer.")
            win.destroy()
            
        def reset():
            self.redundancy_level = 1
            self.status_var.set("Ready. Encryption Level: 1X")
            messagebox.showinfo("Reset", "Encryption set to Standard (1X).")
            win.destroy()

        btn_frame = tk.Frame(win)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Apply", command=apply).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Disable/Reset", command=reset).pack(side=tk.LEFT, padx=5)

    def open_key_manager(self):
        win = tk.Toplevel(self.root)
        win.title("Key Manager")
        win.geometry("400x300")
        
        lbl = tk.Label(win, text="Current Session Key (Memory):")
        lbl.pack(pady=5)
        
        key_display = scrolledtext.ScrolledText(win, height=8, width=40)
        if self.last_used_key:
            key_display.insert(tk.END, json.dumps(self.last_used_key))
        else:
            key_display.insert(tk.END, "No key generated/loaded yet.")
        key_display.config(state=tk.DISABLED)
        key_display.pack(pady=5)
        
        def export_key():
            if not self.last_used_key:
                messagebox.showerror("Error", "No key to export.")
                return
            path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Key", "*.json")])
            if path:
                with open(path, 'w') as f:
                    json.dump(self.last_used_key, f)
                messagebox.showinfo("Success", "Key exported successfully.")

        def clear_key():
            if self.last_used_key:
                resp = messagebox.askyesno("Backup?", "Do you want to backup the key before clearing?")
                if resp:
                    export_key()
            self.last_used_key = None
            key_display.config(state=tk.NORMAL)
            key_display.delete(1.0, tk.END)
            key_display.insert(tk.END, "Key cleared.")
            key_display.config(state=tk.DISABLED)

        btn_frame = tk.Frame(win)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Export Key", command=export_key).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Clear/Generate New", command=clear_key).pack(side=tk.LEFT, padx=5)

    def save_file(self):
        text_content = self.text_area.get("1.0", tk.END + "-1c") # Get all text
        if not text_content:
            messagebox.showwarning("Empty", "Nothing to save.")
            return

        # Perform Encryption
        # We assume if redundancy_level > 1, we use it. 
        # If it is 1, we do standard (which is just 1 loop in our engine logic).
        
        try:
            encrypted_data, key = self.engine.perform_redundant_encryption(text_content, self.redundancy_level)
            
            # Auto-save key to memory
            self.last_used_key = key
            
            file_path = filedialog.asksaveasfilename(defaultextension=".tnp", filetypes=[("Total Notepad Encrypted", "*.tnp")])
            if file_path:
                with open(file_path, 'w') as f:
                    f.write(encrypted_data)
                
                # Prompt user about the key
                response = messagebox.askyesno("Encryption Successful", "File Saved.\n\nThe unique Key used is currently stored in memory.\nDo you want to save the Key file now?\n(You need this to open the file later!)")
                if response:
                    key_path = filedialog.asksaveasfilename(initialfile=os.path.basename(file_path)+".key.json", defaultextension=".json")
                    if key_path:
                        with open(key_path, 'w') as f:
                            json.dump(key, f)
        except Exception as e:
            messagebox.showerror("Encryption Error", str(e))

    def open_file(self):
        # 1. Ask for Encrypted File
        file_path = filedialog.askopenfilename(filetypes=[("Total Notepad Encrypted", "*.tnp"), ("All Files", "*.*")])
        if not file_path:
            return
        
        with open(file_path, 'r') as f:
            encrypted_content = f.read()

        # 2. Determine Key
        key_to_use = None
        
        # Option A: Use memory key
        if self.last_used_key:
            use_mem = messagebox.askyesno("Key Detected", "A key is currently loaded in memory. Use this key?")
            if use_mem:
                key_to_use = self.last_used_key
        
        # Option B: Load key from file
        if not key_to_use:
            key_path = filedialog.askopenfilename(title="Select Key File", filetypes=[("JSON Key", "*.json")])
            if not key_path:
                return # Cancelled
            with open(key_path, 'r') as f:
                key_to_use = json.load(f)
                self.last_used_key = key_to_use # Update memory
        
        # 3. Decrypt
        try:
            decrypted_text = self.engine.perform_redundant_decryption(encrypted_content, key_to_use)
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", decrypted_text)
            messagebox.showinfo("Success", "File decrypted successfully.")
            
            # Check for Redundancy in key to update UI status
            if isinstance(key_to_use[-1], str) and key_to_use[-1].startswith("r="):
                r_val = int(key_to_use[-1].split("=")[1])
                self.status_var.set(f"File Opened. Detected Redundancy Level: {r_val}X")
                self.redundancy_level = r_val # Auto-switch mode
            else:
                self.status_var.set(f"File Opened. Standard Encryption.")
                self.redundancy_level = 1

        except Exception as e:
            messagebox.showerror("Decryption Failed", f"Could not decrypt file.\nCheck if the Key is correct.\n\nError: {str(e)}")

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = TotalNotepadApp(root)
    root.mainloop()
