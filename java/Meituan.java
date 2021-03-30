public class Meituan {

    public static final String WRONG = "Wrong";

    public static final Integer ACCEPT = "Accept";

    public String getUserName(String username) {
        char prefix = username.charAt(0);

    }

    public static int parseInt(String s, int radix) throws NumberFormatException {
        /*
         * WARNING: This method may be invoked early during VM initialization before
         * IntegerCache is initialized. Care must be taken to not use the valueOf
         * method.
         */

        if (s == null) {
            throw new NumberFormatException("null");
        }

        if (radix < Character.MIN_RADIX) {
            throw new NumberFormatException("radix " + radix + " less than Character.MIN_RADIX");
        }

        if (radix > Character.MAX_RADIX) {
            throw new NumberFormatException("radix " + radix + " greater than Character.MAX_RADIX");
        }

        boolean negative = false;
        int i = 0, len = s.length();
        int limit = -Integer.MAX_VALUE;

        if (len > 0) {
            char firstChar = s.charAt(0);
            if (firstChar < '0') { // Possible leading "+" or "-"
                if (firstChar == '-') {
                    negative = true;
                    limit = Integer.MIN_VALUE;
                } else if (firstChar != '+') {
                    throw NumberFormatException.forInputString(s);
                }

                if (len == 1) { // Cannot have lone "+" or "-"
                    throw NumberFormatException.forInputString(s);
                }
                i++;
            }
            int multmin = limit / radix;
            int result = 0;
            while (i < len) {
                // Accumulating negatively avoids surprises near MAX_VALUE
                int digit = Character.digit(s.charAt(i++), radix);
                if (digit < 0 || result < multmin) {
                    throw NumberFormatException.forInputString(s);
                }
                result *= radix;
                if (result < limit + digit) {
                    throw NumberFormatException.forInputString(s);
                }
                result -= digit;
            }
            return negative ? result : -result;
        } else {
            throw NumberFormatException.forInputString(s);
        }
    }

    public static int myParseInt(String s, int radix) throws NumberFormatException {

        if (s == null) {
            throw new NumberFormatException("null");
        }

        if (radix < 2) {
            throw new NumberFormatException("radix " + radix + " less the min radix 2");
        }

        if (radix > 36) {
            throw new NumberFormatException("radix " + radix + " larger than max radix 36");
        }

        boolean negative = false;
        int i = 0, len = s.length();
        int limit = -2^31 + 1;
        
        if (len > 0) {
            char firstChar = s.charAt(0);
            if (firstChar < '0') {
                if (firstChar == '-') {
                    negative = true;
                    limit = -2^32;
                    if (len == 1) {
                        throw new NumberFormatException("For input string: " + s);
                    }
                } else if (firstChar == '+') {
                    if (len == 1) {
                        throw new NumberFormatException("For input string: " + s);
                    }
                } else {
                    throw new NumberFormatException("For input string: " + s);
                }
                i++;
            }
            int multmin = limit / radix;
            int result = 0;
            while (i < len) {
                int digit = Character.digit(s.charAt(i++), radix);
                if (digit < 0 || result < multmin) {
                    throw new NumberFormatException("For input string: " + s);
                }
                result *= radix;
                if (result < limit + digit) {
                    throw new NumberFormatException("For input string: " + s);
                }
                result -= digit;
            }
            return negative ? result : -result;
        } else {
            throw new NumberFormatException("For input string: " + s);
        }
    }
}
