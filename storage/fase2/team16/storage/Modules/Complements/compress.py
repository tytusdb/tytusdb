# Storage Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16

import zlib as zl


class Compression:
    def __init__(self, level, encoding):
        self.level = level
        self.encoding = encoding

    def compress(self, content):
        result = []
        for tupla in content:
            aux = []
            for columna in tupla:
                try:
                    int(columna)
                except:
                    try:
                        float(columna)
                    except:
                        columna = zl.compress(columna.encode(self.encoding), self.level).hex()
                finally:
                    aux.append(columna)
            result.append(aux)
        return result

    def compressDict(self, content: dict):
        for key in content:
            columna = content.get(key)
            try:
                int(columna)
            except:
                try:
                    float(columna)
                except:
                    columna = zl.compress(columna.encode(self.encoding), self.level).hex()
            finally:
                content[key] = columna
        return content

    def compressText(self, text: str):
        try:
            int(text)
        except:
            try:
                float(text)
            except:
                text = zl.compress(text.encode(self.encoding), self.level).hex()
        finally:
            return text

    def decompress(self, content):
        result = []
        for tupla in content:
            aux = []
            for columna in tupla:
                try:
                    int(columna)
                except:
                    try:
                        float(columna)
                    except:
                        columna = columna = zl.decompress(bytes.fromhex(columna)).decode(self.encoding)
                finally:
                    aux.append(columna)
            result.append(aux)
        return result
