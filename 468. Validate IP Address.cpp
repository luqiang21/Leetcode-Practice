class Solution {
public:
    // regex
    string validIPAddress11(string IP) {
        string v4 = "([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])";
        string v6 = "([0-9a-fA-F]{1,4})";
        regex ipv4("(" + v4 + "\\.){3}" + v4);
        regex ipv6("(" + v6 + "\\:){7}" + v6);
        if (regex_match(IP, ipv4)) return "IPv4";
        else if (regex_match(IP, ipv6)) return "IPv6";
        return "Neither";
        
    }
    // divide and conquer
public:
    string validIPAddress(string IP) {
        return validIPv4(IP) ? "IPv4" : (validIPv6(IP) ? "IPv6" : "Neither");
    }
private:
    bool validIPv4(string IP) {
        if (count(IP.begin(), IP.end(), '.') != 3) {
            return false;
        }
        vector<string> parts = split(IP, '.');
        if (parts.size() != 4) {
            return false;
        }
        for (string part : parts) {
            if (part.empty() || part.size() > 3 || part.size() > 1 && part[0] == '0') {
                return false;
            }
            for (char c : part) {
                if (!isdigit(c)) {
                    return false;
                }
            }
            if (stoi(part) > 255) {
                return false;
            }
        }
        return true;
    }
    
    bool validIPv6(string IP) {
        if (count(IP.begin(), IP.end(), ':') != 7) {
            return false;
        }
        vector<string> parts = split(IP, ':');
        if (parts.size() != 8) {
            return false;
        }
        for (string part : parts) {
            if (part.empty() || part.size() > 4) {
                return false;
            }
            for (char c : part) {
                if (!isdigit(c) && (!isalpha(c) || toupper(c) > 'F')) {
                    return false;
                }
            }
        }
        return true;
    }
    
    vector<string> split(string s, char c) {
        vector<string> parts;
        string part;
        istringstream in(s);
        while (getline(in, part, c)) {
            parts.push_back(part);
        }
        return parts;
    }
public:
    string validIPAddress1(string IP) {
        stringstream check1(IP); 
        string intermediate; 
        int n = 0;
        if (IP.find(".") != string::npos) {
            // possible v4
            while(getline(check1, intermediate, '.')) 
            { 
                if (intermediate == "") return "Neither";
                if (!isDigits(intermediate, true)) return "Neither";
                int num = stoi(intermediate);
                if (num > 255 or num < 0) return "Neither";
                if (to_string(num) != intermediate) return "Neither";
                n ++;
            } 
            
            if (n == 4 && std::count(IP.begin(), IP.end(), '.') == 3) return "IPv4";
            return "Neither";
        }
        
        while(getline(check1, intermediate, ':')) 
        { 
            if (intermediate == "") return "Neither";
            if (!isDigits(intermediate, false)) return "Neither";

            if (intermediate.length() > 4) return "Neither";
            int num = stoi(intermediate, nullptr, 16);
            if (num > 65535 or num < 0) return "Neither";
            n ++;
        } 
        if (n == 8 && std::count(IP.begin(), IP.end(), ':') == 7) return "IPv6";
        return "Neither";
    }
    
private:
    bool isDigits(string part, bool isV4) {
        if (isV4 && part.length() > 3) return false;
        if (!isV4 && part.length() > 4) return false;
        for (char c : part) {
            if (!isdigit(c)) {
                if (isV4) return false;
                else {
                    if (!isalpha(c) || toupper(c) > 'F') return false;
                }
            }
        }
        return true;
    }
};
