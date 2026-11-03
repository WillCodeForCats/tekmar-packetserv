r"""Packet object.

Basically a packet has a type and some data and is represented in two
forms: its raw (object) form and in string form.

In string form, it looks like a sequence of hex bytes, e.g.
    0102030F\n

The 01 is the packet type and 02, 03, and 0F is the packet data.  A
packet is always delimited by a newline character (in string form).
"""

# ******************************************************************************
from fields import FieldList, Int8

# ******************************************************************************
# Supported packet types.

(
    TYPE_GENERAL,
    TYPE_TN4,
    TYPE_HW_OVR_TEXT,
    TYPE_HW_OVR_BINARY,
    TYPE_DISPLAY,
    TYPE_NVM,
    TYPE_TRPC,
) = list(range(7))


# ******************************************************************************
class Packet:
    """A packet type and its data bytes."""

    # --------------------------------------------------------------------------
    format = FieldList("PacketFormat", Int8(None))

    # --------------------------------------------------------------------------
    def __init__(self, type=TYPE_GENERAL, data=None):
        """Create a packet with the given type and list of data bytes."""
        self.type = type
        self.data = data if data is not None else []

    # --------------------------------------------------------------------------
    def __str__(self):
        """Create a string-representation of the packet (see the module docs)."""
        lst = ["%02X" % b for b in self.joined()]
        lst.append("\n")
        return "".join(lst)

    # --------------------------------------------------------------------------
    def joined(self):
        """Join the type and data into a single sequence and return it."""
        lst = [self.type]
        lst.extend(self.data)
        return lst

    # --------------------------------------------------------------------------
    @staticmethod
    def from_str(s):
        """Convert a packet in string form (see the module docs) to a Packet.

        Return the resulting packet object.
        """
        ln = len(s)
        if ln & 1:
            ln -= 1
        if ln == 0:
            return Packet()
        try:
            pkt_type, data = Packet.format.unpack(
                [int(x, 16) for x in [s[idx : idx + 2] for idx in range(0, ln, 2)]]
            )
            return Packet(pkt_type[0], data)
        except ValueError:
            return Packet()
