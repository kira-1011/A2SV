class Solution:

    # Function to split the count paired domain into the visit_count and the domain
    def splitDomain(self,count_paired_domain):

        splitted_domain = count_paired_domain.split(" ")
        visit_count = int(splitted_domain[0])
        levels = sep_domain[1].split(".")

        return domain, visit_count

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        cpdomain_visit_count = defaultdict(int)
        count_paired_domains = []

        # Count the total visit_count of each sub level domain
        for cpdomain in cpdomains:

            domain, visit_count = splitDomain(cpdomain)
            sub_levels = ""
            levels = domain.split(".")
            level_len = len(levels)

            for level_idx in range(level_len - 1, -1, -1):

                if sub_levels != "":
                    sub_levels = levels[level_idx] + "." + sub_levels
                
                else:
                    sub_levels += levels[level_idx]
                
                cpdomain_visit_count[sub_levels] += count
        
        # Concatenate the count and domain and append it to a list
        for key, value in cpdomain_visit_count.items():
            count_paired_domains.append(str(value) + " " + key)

        return count_paired_domains