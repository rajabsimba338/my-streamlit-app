import streamlit as st

# Page config
st.set_page_config(
    page_title="ICD-10 Chapter 1 - Infectious Diseases",
    page_icon="💉",
    layout="wide"
)

# Title
st.markdown(
    """
    <style>
    .centered-title {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
        font-size: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="centered-title">ICD-AI HUB</div>', unsafe_allow_html=True)
st.markdown('<div class="centered-title">(CHAPTER 1 - Certain Infectious and Parasitic Diseases)</div>', unsafe_allow_html=True)

# ICD-10 Chapter 1 data structure
icd_10_chapter_1 = {
"A00-A09": {
        "block_description": "Intestinal infectious diseases",
        "categories": {
            "A00": {
                "description": "Cholera",
                "subcategories": {
                    "A00.0": "Cholera due to Vibrio cholerae 01, biovar cholerae",
                    "A00.1": "Cholera due to Vibrio cholerae 01, biovar eltor",
                    "A00.9": "Cholera, unspecified"
                }
            },
            "A01": {
                "description": "Typhoid and paratyphoid fevers",
                "subcategories": {
                    "A01.0": "Typhoid fever",
                    "A01.1": "Paratyphoid fever A",
                    "A01.2": "Paratyphoid fever B",
                    "A01.3": "Paratyphoid fever C",
                    "A01.4": "Paratyphoid fever, unspecified"
                }
            },
            "A02": {
                "description": "Other salmonella infections",
                "subcategories": {
                    "A02.0": "Salmonella enteritis",
                    "A02.1": "Salmonella sepsis",
                    "A02.2": "Localized salmonella infections",
                    "A02.8": "Other specified salmonella infections",
                    "A02.9": "Salmonella infection, unspecified"
                }
            },
            "A03": {
                "description": "Shigellosis",
                "subcategories": {
                    "A03.0": "Shigellosis due to Shigella dysenteriae",
                    "A03.1": "Shigellosis due to Shigella flexneri",
                    "A03.2": "Shigellosis due to Shigella boydii",
                    "A03.3": "Shigellosis due to Shigella sonnei",
                    "A03.8": "Other shigellosis",
                    "A03.9": "Shigellosis, unspecified"
                }
            },
            "A04": {
                "description": "Other bacterial intestinal infections",
                "subcategories": {
                    "A04.0": "Enteropathogenic Escherichia coli infection",
                    "A04.1": "Enterotoxigenic Escherichia coli infection",
                    "A04.2": "Enteroinvasive Escherichia coli infection",
                    "A04.3": "Enterohemorrhagic Escherichia coli infection",
                    "A04.4": "Other intestinal Escherichia coli infections",
                    "A04.5": "Campylobacter enteritis",
                    "A04.6": "Enteritis due to Yersinia enterocolitica",
                    "A04.7": "Enterocolitis due to Clostridium difficile",
                    "A04.8": "Other specified bacterial intestinal infections",
                    "A04.9": "Bacterial intestinal infection, unspecified"
                }
            },
            "A05": {
                "description": "Other bacterial foodborne intoxications, not elsewhere classified",
                "subcategories": {
                    "A05.0": "Foodborne staphylococcal intoxication",
                    "A05.1": "Botulism",
                    "A05.2": "Foodborne Clostridium perfringens [Clostridium welchii] intoxication",
                    "A05.3": "Foodborne Vibrio parahaemolyticus intoxication",
                    "A05.4": "Foodborne Bacillus cereus intoxication",
                    "A05.8": "Other specified bacterial foodborne intoxications",
                    "A05.9": "Bacterial foodborne intoxication, unspecified"
                }
            },
            "A06": {
                "description": "Amoebiasis",
                "subcategories": {
                    "A06.0": "Acute amoebic dysentery",
                    "A06.1": "Chronic intestinal amoebiasis",
                    "A06.2": "Amoebic nondysenteric colitis",
                    "A06.3": "Amoeboma of intestine",
                    "A06.4": "Amoebic liver abscess",
                    "A06.5": "Amoebic lung abscess",
                    "A06.6": "Amoebic brain abscess",
                    "A06.7": "Cutaneous amoebiasis",
                    "A06.8": "Amoebiasis of other sites",
                    "A06.9": "Amoebiasis, unspecified"
                }
            },
            "A07": {
                "description": "Other protozoal intestinal diseases",
                "subcategories": {
                    "A07.0": "Balantidiasis",
                    "A07.1": "Giardiasis [lambliasis]",
                    "A07.2": "Cryptosporidiosis",
                    "A07.3": "Isosporiasis",
                    "A07.8": "Other specified protozoal intestinal diseases",
                    "A07.9": "Protozoal intestinal disease, unspecified"
                }
            },
            "A08": {
                "description": "Viral and other specified intestinal infections",
                "subcategories": {
                    "A08.0": "Rotaviral enteritis",
                    "A08.1": "Acute gastroenteropathy due to Norwalk agent",
                    "A08.2": "Adenoviral enteritis",
                    "A08.3": "Other viral enteritis",
                    "A08.4": "Viral intestinal infection, unspecified",
                    "A08.5": "Other specified intestinal infections"
                }
            },
            "A09": {
                "description": "Infectious gastroenteritis and colitis, unspecified",
                "subcategories": {
                    "A09.0": "Infectious gastroenteritis and colitis, unspecified"
                }
            }
        }
    },
    "A15-A19": {
        "block_description": "Tuberculosis",
        "categories": {
            "A15": {
                "description": "Respiratory tuberculosis, bacteriologically and histologically confirmed",
                "subcategories": {
                    "A15.0": "Tuberculosis of lung",
                    "A15.1": "Tuberculosis of trachea and bronchus",
                    "A15.2": "Tuberculous laryngitis",
                    "A15.3": "Tuberculosis of other respiratory organs",
                    "A15.4": "Tuberculosis of intrathoracic lymph nodes",
                }
            },
            "A16": {
                "description": "Respiratory tuberculosis, not confirmed bacteriologically or histologically",
                "subcategories": {
                    "A16.0": "Tuberculosis of lung, without confirmation",
                    "A16.1": "Tuberculosis of trachea and bronchus, without confirmation",
                    "A16.2": "Tuberculosis of larynx, without confirmation",
                    "A16.3": "Tuberculosis of other respiratory organs, without confirmation",
                    "A16.4": "Tuberculosis of intrathoracic lymph nodes, without confirmation",
                }
            },
            "A17": {
                "description": "Tuberculosis of nervous system",
                "subcategories": {
                    "A17.0": "Tuberculous meningitis",
                    "A17.1": "Meningeal tuberculoma",
                    "A17.8": "Other tuberculosis of nervous system",
                    "A17.9": "Tuberculosis of nervous system, unspecified"
                }
            },
            "A18": {
                "description": "Tuberculosis of other organs",
                "subcategories": {
                    "A18.0": "Tuberculosis of bones and joints",
                    "A18.1": "Tuberculosis of genitourinary system",
                    "A18.2": "Tuberculous peripheral lymphadenopathy",
                    "A18.3": "Tuberculosis of intestines, peritoneum, and mesenteric glands",
                    "A18.4": "Tuberculosis of skin and subcutaneous tissue",
                    "A18.5": "Tuberculosis of eye",
                    "A18.6": "Tuberculosis of ear",
                    "A18.7": "Other specified tuberculosis of organs",
                    "A18.8": "Tuberculosis of other organs, unspecified"
                }
            },
            "A19": {
                "description": "Miliary tuberculosis",
                "subcategories": {
                    "A19.0": "Miliary tuberculosis, unspecified"
                }
            }
        }
    },
    "A20-A28": {
        "block_description": "Certain zoonotic bacterial diseases",
        "categories": {
            "A20": {
                "description": "Plague",
                "subcategories": {
                    "A20.0": "Bubonic plague",
                    "A20.1": "Pneumonic plague",
                    "A20.9": "Plague, unspecified"
                }
            },
            "A21": {
                "description": "Tularemia",
                "subcategories": {
                    "A21.0": "Tularemia, unspecified",
                    "A21.1": "Ulceroglandular tularemia",
                    "A21.2": "Glandular tularemia",
                    "A21.3": "Pneumonic tularemia",
                    "A21.4": "Oculoglandular tularemia",
                    "A21.5": "Typhoidal tularemia",
                    "A21.8": "Other forms of tularemia"
                }
            },
            "A22": {
                "description": "Anthrax",
                "subcategories": {
                    "A22.0": "Cutaneous anthrax",
                    "A22.1": "Pulmonary anthrax",
                    "A22.2": "Gastrointestinal anthrax",
                    "A22.8": "Other forms of anthrax"
                }
            },
            "A23": {
                "description": "Brucellosis",
                "subcategories": {
                    "A23.0": "Brucellosis due to Brucella melitensis",
                    "A23.1": "Brucellosis due to Brucella abortus",
                    "A23.9": "Brucellosis, unspecified"
                }
            },
            "A24": {
                "description": "Glanders",
                "subcategories": {
                    "A24.0": "Glanders, unspecified",
                    "A24.1": "Pulmonary glanders",
                    "A24.2": "Cutaneous glanders"
                }
            },
            "A25": {
                "description": "Rat-bite fever",
                "subcategories": {
                    "A25.0": "Rat-bite fever, unspecified",
                    "A25.1": "Haverhill fever"
                }
            },
            "A26": {
                "description": "Erysipeloid",
                "subcategories": {
                    "A26.0": "Erysipeloid, unspecified",
                    "A26.1": "Erysipeloid due to Erysipelothrix rhusiopathiae"
                }
            },
            "A27": {
                "description": "Leptospirosis",
                "subcategories": {
                    "A27.0": "Leptospirosis, unspecified",
                    "A27.1": "Weil's disease"
                }
            },
            "A28": {
                "description": "Other zoonotic bacterial diseases",
                "subcategories": {
                    "A28.0": "Other zoonotic bacterial diseases, unspecified"
                }
            }
        }
    },
    "A30-A99": {
        "block_description": "Other infectious diseases",
        "categories": {
            "A30": {
                "description": "Leprosy",
                "subcategories": {
                    "A30.0": "Leprosy, tuberculoid",
                    "A30.1": "Leprosy, lepromatous",
                    "A30.2": "Leprosy, unspecified"
                }
            },
            "A31": {
                "description": "Infection due to other mycobacteria",
                "subcategories": {
                    "A31.0": "Infection due to Mycobacterium avium",
                    "A31.1": "Infection due to Mycobacterium intracellulare",
                    "A31.9": "Infection due to other specified mycobacteria"
                }
            },
            "A32": {
                "description": "Listeriosis",
                "subcategories": {
                    "A32.0": "Listeriosis, unspecified",
                    "A32.1": "Septicemia due to Listeria monocytogenes"
                }
            },
            "A33": {
                "description": "Congenital listeriosis",
                "subcategories": {
                    "A33.0": "Congenital listeriosis, unspecified"
                }
            },
            "A34": {
                "description": "Obstetric listeriosis",
                "subcategories": {
                    "A34.0": "Obstetric listeriosis, unspecified"
                }
            },
            "A35": {
                "description": "Tetanus",
                "subcategories": {
                    "A35.0": "Tetanus neonatorum",
                    "A35.1": "Other tetanus"
                }
            },
            "A36": {
                "description": "Diphtheria",
                "subcategories": {
                    "A36.0": "Diphtheria, unspecified",
                    "A36.1": "Respiratory diphtheria",
                    "A36.2": "Cutaneous diphtheria"
                }
            },
            "A37": {
                "description": "Whooping cough",
                "subcategories": {
                    "A37.0": "Whooping cough, unspecified",
                    "A37.1": "Whooping cough due to Bordetella pertussis",
                    "A37.9": "Whooping cough, unspecified"
                }
            },
            "A38": {
                "description": "Scarlet fever",
                "subcategories": {
                    "A38.0": "Scarlet fever, unspecified"
                }
            },
           "A39": {
                "description": "Meningococcal infection",
                "subcategories": {
                    "A39.0": "Meningococcal meningitis",
                    "A39.1": "Meningococcal septicemia",
                    "A39.9": "Meningococcal infection, unspecified"
                }
            },
            "A40": {
                "description": "Streptococcal sepsis",
                "subcategories": {
                    "A40.0": "Streptococcal sepsis due to group A Streptococcus",
                    "A40.1": "Streptococcal sepsis due to group B Streptococcus",
                    "A40.2": "Streptococcal sepsis due to other Streptococcus",
                    "A40.8": "Other streptococcal sepsis",
                    "A40.9": "Streptococcal sepsis, unspecified"
                }
            },
            "A41": {
                "description": "Other sepsis",
                "subcategories": {
                    "A41.0": "Sepsis due to Staphylococcus aureus",
                    "A41.1": "Sepsis due to other specified bacteria",
                    "A41.9": "Sepsis, unspecified"
                }
            },
            "A42": {
                "description": "Actinomycosis",
                "subcategories": {
                    "A42.0": "Actinomycosis, unspecified",
                    "A42.1": "Cervicofacial actinomycosis",
                    "A42.2": "Thoracic actinomycosis",
                    "A42.3": "Abdominal actinomycosis",
                    "A42.8": "Other specified actinomycosis"
                }
            },
            "A43": {
                "description": "Nocardiosis",
                "subcategories": {
                    "A43.0": "Nocardiosis, unspecified"
                }
            },
            "A44": {
                "description": "Ehrlichiosis and anaplasmosis",
                "subcategories": {
                    "A44.0": "Ehrlichiosis due to Ehrlichia chaffeensis",
                    "A44.1": "Anaplasmosis due to Anaplasma phagocytophilum",
                    "A44.9": "Ehrlichiosis and anaplasmosis, unspecified"
                }
            },
            "A45": {
                "description": "Relapsing fever",
                "subcategories": {
                    "A45.0": "Relapsing fever due to Borrelia recurrentis",
                    "A45.1": "Relapsing fever due to other Borrelia",
                    "A45.9": "Relapsing fever, unspecified"
                }
            },
            "A46": {
                "description": "Cellulitis and abscess due to Staphylococcus aureus",
                "subcategories": {
                    "A46.0": "Cellulitis due to Staphylococcus aureus",
                    "A46.1": "Abscess due to Staphylococcus aureus"
                }
            },
            "A47": {
                "description": "Other infections due to other specified bacteria",
                "subcategories": {
                    "A47.0": "Other specified infections due to Staphylococcus",
                    "A47.1": "Other specified infections due to Streptococcus"
                }
            },
            "A48": {
                "description": "Other bacterial infections, not elsewhere classified",
                "subcategories": {
                    "A48.0": "Other specified bacterial infections"
                }
            },
            "A49": {
                "description": "Unspecified bacterial infection",
                "subcategories": {
                    "A49.0": "Unspecified bacterial infection"
                }
            },
            "A50": {
                "description": "Congenital syphilis",
                "subcategories": {
                    "A50.0": "Congenital syphilis, early",
                    "A50.1": "Congenital syphilis, late",
                    "A50.9": "Congenital syphilis, unspecified"
                }
            },
            "A51": {
                "description": "Primary syphilis",
                "subcategories": {
                    "A51.0": "Primary syphilis, unspecified",
                    "A51.1": "Primary syphilis, in pregnant women"
                }
            },
            "A52": {
                "description": "Secondary syphilis",
                "subcategories": {
                    "A52.0": "Secondary syphilis, unspecified",
                    "A52.1": "Secondary syphilis, in pregnant women"
                }
            },
            "A53": {
                "description": "Latent syphilis",
                "subcategories": {
                    "A53.0": "Latent syphilis, unspecified",
                    "A53.1": "Latent syphilis, in pregnant women"
                }
            },
            "A54": {
                "description": "Tertiary syphilis",
                "subcategories": {
                    "A54.0": "Tertiary syphilis, unspecified",
                    "A54.1": "Tertiary syphilis, in pregnant women"
                }
            },
            "A55": {
                "description": "Neurological syphilis",
                "subcategories": {
                    "A55.0": "Neurological syphilis, unspecified"
                }
            },
            "A56": {
                "description": "Chlamydia infections",
                "subcategories": {
                    "A56.0": "Chlamydia infection of cervix uteri",
                    "A56.1": "Chlamydia infection of rectum",
                    "A56.2": "Chlamydia infection of oropharynx",
                    "A56.3": "Chlamydia infection of urethra",
                    "A56.4": "Chlamydia infection of eye",
                    "A56.5": "Chlamydia infection of other sites"
                }
            },
            "A57": {
                "description": "Trichomoniasis",
                "subcategories": {
                    "A57.0": "Trichomoniasis, unspecified"
                }
            },
            "A58": {
                "description": "Other protozoal infections",
                "subcategories": {
                    "A58.0": "Other protozoal infections, unspecified"
                }
            },
            "A59": {
                "description": "Infection by an unspecified virus",
                "subcategories": {
                    "A59.0": "Infection by an unspecified virus"
                }
            },
            "A60": {
                "description": "Anogenital herpesviral infection",
                "subcategories": {
                    "A60.0": "Anogenital herpesviral infection, unspecified",
                    "A60.1": "Herpesviral infection of vulva",
                    "A60.2": "Herpesviral infection of vagina",
                    "A60.3": "Herpesviral infection of penis"
                }
            },
            "A61": {
                "description": "Human papillomavirus (HPV) infections",
                "subcategories": {
                    "A61.0": "HPV infection, unspecified"
                }
            },
            "A62": {
                "description": "Infection by other specified virus",
                "subcategories": {
                    "A62.0": "Infection by other specified virus, unspecified"
                }
            },
            "A63": {
                "description": "Other specified infections",
                "subcategories": {
                    "A63.0": "Other specified infections"
                }
            },
            "A64": {
                "description": "Unspecified infection",
                "subcategories": {
                    "A64.0": "Unspecified infection"
                }
            },
            "A65": {
                "description": "Other diseases due to chlamydiae",
                "subcategories": {
                    "A65.0": "Other diseases due to chlamydiae, unspecified"
                }
            },
            "A66": {
                "description": "Other diseases due to other specified organisms",
                "subcategories": {
                    "A66.0": "Other diseases due to other specified organisms, unspecified"
                }
            },
            "A67": {
                "description": "Infection due to other organisms",
                "subcategories": {
                    "A67.0": "Infection due to other organisms, unspecified"
                }
            },
            "A68": {
                "description": "Infections of unspecified organisms",
                "subcategories": {
                    "A68.0": "Infections of unspecified organisms, unspecified"
                }
            },
            "A69": {
                "description": "Other diseases due to zoonotic organisms",
                "subcategories": {
                    "A69.0": "Other diseases due to zoonotic organisms, unspecified"
                }
            },
            "A70": {
                "description": "Mycoplasma infections",
                "subcategories": {
                    "A70.0": "Mycoplasma pneumonia, unspecified",
                    "A70.1": "Mycoplasma genitalium infection"
                }
            },
            "A71": {
                "description": "Coxiella burnetii infection",
                "subcategories": {
                    "A71.0": "Coxiella burnetii infection, unspecified"
                }
            },
            "A72": {
                "description": "Chancroid",
                "subcategories": {
                    "A72.0": "Chancroid, unspecified"
                }
            },
            "A73": {
                "description": "Granuloma inguinale",
                "subcategories": {
                    "A73.0": "Granuloma inguinale, unspecified"
                }
            },
            "A74": {
                "description": "Other diseases caused by organisms, not elsewhere classified",
                "subcategories": {
                    "A74.0": "Other diseases caused by organisms, not elsewhere classified, unspecified"
                }
            },
            "A75": {
                "description": "Rickettsial infections",
                "subcategories": {
                    "A75.0": "Rickettsial infection, unspecified"
                }
            },
            "A76": {
                "description": "Infections by non-HIV viruses",
                "subcategories": {
                    "A76.0": "Infection by non-HIV viruses, unspecified"
                }
            },
            "A77": {
                "description": "Infection by other non-HIV virus",
                "subcategories": {
                    "A77.0": "Infection by other non-HIV virus, unspecified"
                }
            },
            "A78": {
                "description": "Infection due to other non-viral organisms",
                "subcategories": {
                    "A78.0": "Infection due to other non-viral organisms, unspecified"
                }
            },
            "A79": {
                "description": "Infection due to unspecified organism",
                "subcategories": {
                    "A79.0": "Infection due to unspecified organism"
                }
            },
            "A80": {
                "description": "Acute poliomyelitis",
                "subcategories": {
                    "A80.0": "Acute poliomyelitis, unspecified"
                }
            },
            "A81": {
                "description": "Atypical virus infections of the central nervous system",
                "subcategories": {
                    "A81.0": "Atypical virus infections of the central nervous system, unspecified"
                }
            },
            "A82": {
                "description": "Rabies",
                "subcategories": {
                    "A82.0": "Rabies, unspecified"
                }
            },
            "A83": {
                "description": "Viral hemorrhagic fevers",
                "subcategories": {
                    "A83.0": "Viral hemorrhagic fever, unspecified"
                }
            },
            "A84": {
                "description": "Viral encephalitis",
                "subcategories": {
                    "A84.0": "Viral encephalitis, unspecified"
                }
            },
            "A85": {
                "description": "Other viral infections of the central nervous system",
                "subcategories": {
                    "A85.0": "Other viral infections of the central nervous system, unspecified"
                }
            },
            "A86": {
                "description": "Unspecified viral infection of the central nervous system",
                "subcategories": {
                    "A86.0": "Unspecified viral infection of the central nervous system"
                }
            },
            "A87": {
                "description": "Viral infections of the nervous system, not elsewhere classified",
                "subcategories": {
                    "A87.0": "Viral infections of the nervous system, not elsewhere classified, unspecified"
                }
            },
            "A88": {
                "description": "Other viral infections",
                "subcategories": {
                    "A88.0": "Other viral infections, unspecified"
                }
            },
            "A89": {
                "description": "Unspecified infections",
                "subcategories": {
                    "A89.0": "Unspecified infections"
                }
            },
            "A90": {
                "description": "Dengue fever",
                "subcategories": {
                    "A90.0": "Dengue fever, unspecified"
                }
            },
            "A91": {
                "description": "Dengue hemorrhagic fever",
                "subcategories": {
                    "A91.0": "Dengue hemorrhagic fever, unspecified"
                }
            },
"A92": {
    "description": "Other viral hemorrhagic fevers",
    "subcategories": {
        "A92.0": "Other viral hemorrhagic fever, unspecified"
    }
},
"A93": {
    "description": "Arboviral diseases, except viral hemorrhagic fevers",
    "subcategories": {
        "A93.0": "West Nile virus infection",
        "A93.1": "Chikungunya virus infection",
        "A93.9": "Arboviral infection, unspecified"
    }
},
"A94": {
    "description": "Other arthropod-borne viral fevers",
    "subcategories": {
        "A94.0": "Other arthropod-borne viral fever, unspecified"
    }
},
"A95": {
    "description": "Yellow fever",
    "subcategories": {
        "A95.0": "Yellow fever, unspecified"
    }
},
"A96": {
    "description": "Viral hemorrhagic fevers, not elsewhere classified",
    "subcategories": {
        "A96.0": "Viral hemorrhagic fever, unspecified"
    }
},
"A97": {
    "description": "Viral hepatitis",
    "subcategories": {
        "A97.0": "Viral hepatitis A",
        "A97.1": "Viral hepatitis B",
        "A97.2": "Viral hepatitis C",
        "A97.3": "Viral hepatitis D",
        "A97.4": "Viral hepatitis E",
        "A97.9": "Viral hepatitis, unspecified"
    }
},
"A98": {
    "description": "Other viral diseases",
    "subcategories": {
        "A98.0": "Infection by an unspecified virus",
        "A98.1": "Viral infection of the skin",
        "A98.9": "Other viral diseases, unspecified"
    }
},
"A99": {
    "description": "Unspecified infectious disease",
    "subcategories": {
        "A99.0": "Infectious disease, unspecified"
                }
            }
        }
    }
}

def provide_detailed_info(code):
    detailed_info = {
        "A00": "Cholera is an acute diarrheal illness caused by infection of the intestine with Vibrio cholerae bacteria. It is characterized by profuse watery diarrhea, vomiting, and severe dehydration. Without prompt treatment, cholera can be life-threatening.",
        "A00.0": "Cholera due to Vibrio cholerae 01, biovar cholerae is the most common type of cholera, associated with epidemic outbreaks and characterized by severe dehydration.",
        "A00.1": "Cholera due to Vibrio cholerae 01, biovar eltor is a specific type of cholera infection linked to the eltor biotype of the Vibrio cholerae bacterium, which may cause more severe disease and has been associated with outbreaks.",
        "A00.9": "Cholera, unspecified refers to cases of cholera where the specific type or strain of Vibrio cholerae is not identified or documented, leading to generalized treatment and management protocols.",
        
        "A01": "Typhoid and paratyphoid fevers are bacterial infections caused by Salmonella Typhi and Paratyphi. They are typically transmitted through contaminated food or water and can lead to prolonged high fever, fatigue, and abdominal pain.",
        "A01.0": "Typhoid fever is a serious bacterial infection caused by Salmonella Typhi, leading to prolonged fever, abdominal pain, and systemic symptoms, often requiring hospitalization.",
        "A01.1": "Paratyphoid fever A is a bacterial infection caused by Salmonella Paratyphi A, resulting in symptoms similar to typhoid fever but typically less severe.",
        "A01.2": "Paratyphoid fever B is caused by Salmonella Paratyphi B, presenting symptoms akin to typhoid fever, including fever, headache, and gastrointestinal upset.",
        "A01.3": "Paratyphoid fever C is caused by Salmonella Paratyphi C and can result in similar clinical manifestations as typhoid and other paratyphoid fevers.",
        "A01.4": "Paratyphoid fever, unspecified refers to cases of paratyphoid fever where the specific serotype of Salmonella is not identified, leading to treatment based on general symptoms.",
        
        "A02": "Other salmonella infections include a range of diseases caused by different types of Salmonella bacteria. Commonly, these infections result in gastroenteritis, but they can also cause more severe conditions such as sepsis or localized infections in other organs.",
        "A02.0": "Salmonella enteritis is an infection caused by various Salmonella strains, resulting in diarrhea, abdominal pain, and fever.",
        "A02.1": "Salmonella sepsis refers to the presence of Salmonella bacteria in the bloodstream, which can lead to severe systemic illness.",
        "A02.2": "Localized salmonella infections may occur in organs such as bones or joints, leading to symptoms specific to the affected area.",
        "A02.8": "Other specified salmonella infections include rare types of salmonella infections not covered by the standard categories.",
        "A02.9": "Salmonella infection, unspecified refers to salmonella infections not categorized under specific types or serotypes, requiring general treatment approaches.",
        
        "A03": "Shigellosis is an infection caused by Shigella bacteria. It primarily causes diarrhea, which may be bloody, as well as stomach pain, fever, and nausea. It spreads through contaminated food, water, or direct contact.",
        "A03.0": "Shigellosis due to Shigella dysenteriae leads to severe dysentery, characterized by bloody diarrhea and abdominal cramps.",
        "A03.1": "Shigellosis due to Shigella flexneri is a common cause of bacterial dysentery, often associated with outbreaks in crowded environments.",
        "A03.2": "Shigellosis due to Shigella boydii is less common but can cause similar gastrointestinal symptoms.",
        "A03.3": "Shigellosis due to Shigella sonnei is often linked to milder cases of dysentery but can still lead to severe dehydration.",
        "A03.8": "Other shigellosis refers to cases caused by different or less common species of Shigella.",
        "A03.9": "Shigellosis, unspecified refers to cases of shigellosis where the specific Shigella species is not identified.",
        
        "A04": "Other bacterial intestinal infections, including those caused by Campylobacter, Escherichia coli (E. coli), and other organisms, which can cause symptoms ranging from mild diarrhea to severe illness, including hemolytic uremic syndrome (HUS).",
        "A04.0": "Enteropathogenic Escherichia coli infection leads to diarrhea often associated with outbreaks in infants and young children.",
        "A04.1": "Enterotoxigenic Escherichia coli infection is a common cause of traveler's diarrhea, characterized by watery diarrhea and abdominal cramps.",
        "A04.2": "Enteroinvasive Escherichia coli infection leads to symptoms similar to Shigella infections, including bloody diarrhea.",
        "A04.3": "Enterohemorrhagic Escherichia coli infection can cause severe abdominal cramps, diarrhea, and can lead to HUS.",
        "A04.4": "Other intestinal Escherichia coli infections refer to infections not categorized in the specific subtypes.",
        "A04.5": "Campylobacter enteritis is caused by Campylobacter jejuni and typically results in gastroenteritis, including diarrhea and abdominal pain.",
        "A04.6": "Enteritis due to Yersinia enterocolitica can cause abdominal pain and diarrhea, often resembling appendicitis.",
        "A04.7": "Enterocolitis due to Clostridium difficile often occurs after antibiotic use, leading to severe diarrhea and colitis.",
        "A04.8": "Other specified bacterial intestinal infections include rare or atypical bacterial infections affecting the intestines.",
        "A04.9": "Bacterial intestinal infection, unspecified refers to intestinal infections caused by bacteria that do not fit into specific categories.",
        
        "A05": "Other bacterial foodborne intoxications such as botulism and staphylococcal food poisoning. These are caused by toxins produced by bacteria in improperly stored or prepared food, leading to nausea, vomiting, and sometimes more severe symptoms.",
        "A05.0": "Foodborne staphylococcal intoxication is caused by toxins from Staphylococcus aureus, leading to rapid onset of gastrointestinal symptoms after consuming contaminated food.",
        "A05.1": "Botulism is a rare but serious illness caused by a toxin produced by Clostridium botulinum, leading to muscle paralysis and potentially respiratory failure.",
        "A05.2": "Foodborne Clostridium perfringens intoxication occurs due to eating contaminated food, leading to diarrhea and abdominal cramps.",
        "A05.3": "Foodborne Vibrio parahaemolyticus intoxication is often linked to the consumption of undercooked seafood, resulting in gastrointestinal distress.",
        "A05.4": "Foodborne Bacillus cereus intoxication can lead to two types of illness: one characterized by vomiting and the other by diarrhea.",
        "A05.8": "Other specified bacterial foodborne intoxications refer to cases of foodborne illnesses caused by bacteria not specifically categorized.",
        "A05.9": "Bacterial foodborne intoxication, unspecified refers to cases of foodborne illnesses not specifically identified, often requiring supportive care.",
        
        "A06": "Amebiasis is a parasitic infection caused by Entamoeba histolytica, typically resulting in diarrhea, abdominal pain, and in severe cases, liver abscesses. Transmission occurs via ingestion of cysts from contaminated water or food.",
        "A06.0": "Acute amoebic dysentery is a severe form of amebiasis, characterized by bloody diarrhea and abdominal pain.",
        "A06.1": "Chronic intestinal amoebiasis refers to cases of Entamoeba histolytica infection that present with mild symptoms over an extended period.",
        "A06.2": "Amoebic nondysenteric colitis leads to diarrhea and abdominal pain without severe dysentery.",
        "A06.3": "Amoeboma of intestine refers to a tumor-like mass caused by Entamoeba histolytica in the intestinal tract.",
        "A06.4": "Amoebic liver abscess is a severe complication of amebiasis characterized by pus-filled lesions in the liver.",
        "A06.5": "Amoebic lung abscess refers to lung infections caused by Entamoeba histolytica, usually as a complication of liver abscess.",
        "A06.6": "Amoebic brain abscess is a rare but serious infection affecting the brain caused by Entamoeba histolytica.",
        "A06.7": "Cutaneous amoebiasis refers to skin infections caused by Entamoeba histolytica, typically manifesting as lesions.",
        "A06.8": "Amoebiasis of other sites includes infections outside the gastrointestinal tract caused by Entamoeba histolytica.",
        "A06.9": "Amebiasis, unspecified refers to cases where the specific symptoms or manifestations of amebiasis are not clearly defined.",
        
        "A07": "Other protozoal intestinal diseases include giardiasis and cryptosporidiosis. These diseases are caused by parasitic protozoa and lead to gastrointestinal symptoms such as diarrhea, nausea, and abdominal cramps.",
        "A07.0": "Giardiasis is caused by Giardia lamblia and results in diarrhea, abdominal pain, and nausea, often linked to contaminated water.",
        "A07.1": "Cryptosporidiosis is caused by Cryptosporidium spp. and leads to watery diarrhea, often associated with swimming in contaminated water.",
        "A07.8": "Other specified protozoal intestinal diseases refer to cases caused by protozoa not covered by giardiasis or cryptosporidiosis.",
        "A07.9": "Protozoal intestinal disease, unspecified refers to intestinal infections caused by protozoa that do not fit into specific categories.",
        
        "A08": "Viral and other specified intestinal infections include infections caused by viruses such as norovirus and rotavirus. These infections are often associated with outbreaks and can lead to gastroenteritis.",
        "A08.0": "Acute gastroenteritis due to rotavirus leads to severe diarrhea, vomiting, and dehydration, particularly in young children.",
        "A08.1": "Acute gastroenteritis due to norovirus is characterized by sudden onset of vomiting and diarrhea, often linked to contaminated food or surfaces.",
        "A08.2": "Viral enteritis refers to inflammation of the intestines caused by viral infections, leading to symptoms similar to other gastroenteritis cases.",
        "A08.8": "Other specified viral intestinal infections include rare viral infections affecting the intestines.",
        "A08.9": "Viral intestinal infection, unspecified refers to intestinal infections caused by viruses that are not clearly identified.",
        
        "A09": "Diarrhea and gastroenteritis of unknown cause encompasses cases of diarrhea or gastroenteritis where the specific etiology is not identified, necessitating general treatment approaches.",
        
        "A15": "Respiratory tuberculosis is caused by Mycobacterium tuberculosis and primarily affects the lungs, characterized by chronic cough, chest pain, and hemoptysis.",
        "A15.0": "Pulmonary tuberculosis, unspecified refers to cases of pulmonary tuberculosis where the specifics of the infection are not clearly defined.",
        "A15.1": "Primary respiratory tuberculosis is a form of tuberculosis that occurs in previously uninfected individuals, often presenting with mild respiratory symptoms.",
        "A15.2": "Recurrent pulmonary tuberculosis refers to cases of tuberculosis that reappear after previous treatment.",
        "A15.3": "Respiratory tuberculosis due to other specified organisms includes atypical mycobacterial infections affecting the lungs.",
        
        "A16": "Other respiratory tuberculosis includes tuberculosis that primarily affects organs other than the lungs, potentially leading to systemic symptoms.",
        "A16.0": "Pleural tuberculosis is characterized by tuberculosis affecting the pleura, often leading to pleurisy and respiratory symptoms.",
        "A16.1": "Tuberculoma is a localized mass of tuberculosis infection in the lungs, leading to respiratory symptoms.",
        "A16.2": "Other specified respiratory tuberculosis refers to cases where the specific site or manifestation of the infection is not clearly defined.",
        
        "A17": "Central nervous system tuberculosis includes tuberculosis infections affecting the brain and spinal cord, which can lead to severe neurological symptoms.",
        "A17.0": "Tuberculosis of meninges is characterized by inflammation of the protective membranes covering the brain and spinal cord, leading to symptoms such as headache, fever, and altered consciousness.",
        "A17.1": "Tuberculoma of the brain refers to localized masses of tuberculosis infection in the brain, leading to neurological deficits.",
        "A17.2": "Other specified tuberculosis of central nervous system refers to cases where the specifics of the CNS involvement are not clearly defined.",
        
        "A18": "Other forms of tuberculosis include extrapulmonary tuberculosis affecting various organs and systems outside the lungs.",
        "A18.0": "Tuberculosis of bones and joints is characterized by infection in skeletal tissues, leading to pain, swelling, and potential joint deformities.",
        "A18.1": "Tuberculosis of the genitourinary system refers to infection affecting the urinary and reproductive organs, often leading to pain and dysfunction.",
        "A18.2": "Tuberculous peripheral lymphadenopathy involves the enlargement of lymph nodes due to tuberculosis infection, leading to localized swelling and discomfort.",
        "A18.3": "Tuberculosis of the intestines, peritoneum, and mesenteric glands refers to infections affecting the gastrointestinal system, leading to symptoms such as abdominal pain and gastrointestinal disturbance.",
        "A18.4": "Tuberculosis of skin and subcutaneous tissue involves infections that manifest as skin lesions and ulcers, causing localized inflammation.",
        "A18.5": "Tuberculosis of the eye can lead to ocular complications, potentially resulting in vision impairment or blindness.",
        "A18.6": "Tuberculosis of the ear may involve the external or middle ear, leading to pain and possible hearing loss.",
        "A18.7": "Other specified tuberculosis of organs encompasses cases of tuberculosis affecting various organs not previously specified.",
        "A18.8": "Tuberculosis of other organs, unspecified, refers to cases where the specific organ involvement is not clearly defined.",
        
      
     
        "A19": "Miliary tuberculosis is a severe form of tuberculosis characterized by the dissemination of Mycobacterium tuberculosis through the bloodstream, leading to numerous small lesions in various organs, resembling millet seeds.",
        "A19.0": "Miliary tuberculosis, unspecified refers to cases where the specific details of the miliary tuberculosis infection are not documented, including the absence of specific organ involvement or clinical manifestations.",
        
        "A20": "Plague is a serious infectious disease caused by the bacterium Yersinia pestis, primarily transmitted through flea bites, handling infected animals, or inhaling respiratory droplets from an infected person. It can present in several forms, including bubonic, septicemic, and pneumonic plague.",
        "A20.0": "Bubonic plague is the most common form of plague, characterized by swollen and painful lymph nodes (buboes), fever, chills, and weakness. It is typically transmitted through flea bites.",
        "A20.1": "Pneumonic plague is a severe form of plague that affects the lungs and can be transmitted person-to-person through respiratory droplets. It is characterized by pneumonia symptoms such as cough, chest pain, and difficulty breathing.",
        "A20.9": "Plague, unspecified refers to cases of plague where the specific form or details of the infection are not identified, necessitating general treatment protocols.",
        
     
        "A30": "Leprosy is a chronic infectious disease caused by Mycobacterium leprae, affecting the skin, peripheral nerves, and mucous membranes, leading to skin lesions and potential disability if untreated.",
        "A30.0": "Leprosy, tuberculoid refers to the milder form of leprosy characterized by a few well-defined skin lesions and sensory loss in affected areas.",
        "A30.1": "Leprosy, lepromatous is the more severe form of leprosy with widespread skin lesions, systemic involvement, and a high degree of nerve damage.",
        "A30.2": "Leprosy, unspecified refers to cases of leprosy where the specific type is not documented, requiring general treatment approaches.",
        
        "A31": "Infection due to other mycobacteria includes infections caused by non-tuberculous mycobacteria (NTM) that can lead to pulmonary disease and other systemic infections.",
        "A31.0": "Infection due to Mycobacterium avium indicates an infection primarily affecting immunocompromised individuals, leading to pulmonary and disseminated disease.",
        "A31.1": "Infection due to Mycobacterium intracellulare refers to infections caused by this organism, often associated with similar symptoms as M. avium.",
        "A31.9": "Infection due to other specified mycobacteria indicates infections from other non-tuberculous mycobacteria not specified elsewhere.",
        
        "A32": "Listeriosis is an infection caused by Listeria monocytogenes, primarily transmitted through contaminated food, which can lead to severe illness in vulnerable populations.",
        "A32.0": "Listeriosis, unspecified refers to cases of listeriosis where the specific details of the infection are not documented.",
        "A32.1": "Septicemia due to Listeria monocytogenes indicates the presence of Listeria in the bloodstream, leading to systemic illness.",
        
        "A33": "Congenital listeriosis occurs when a mother transmits Listeria monocytogenes to her baby during pregnancy or childbirth, potentially leading to serious neonatal complications.",
        "A33.0": "Congenital listeriosis, unspecified indicates cases where specific details of the infection are not documented.",
        
        "A34": "Obstetric listeriosis refers to listeriosis occurring during pregnancy, posing risks to both mother and fetus.",
        "A34.0": "Obstetric listeriosis, unspecified indicates cases without specific details about the clinical manifestation.",
        
        "A35": "Tetanus is a serious bacterial infection caused by Clostridium tetani, characterized by muscle stiffness and spasms, which can be life-threatening.",
        "A35.0": "Tetanus neonatorum refers to tetanus infection in newborns, typically resulting from unclean practices during umbilical cord cutting.",
        "A35.1": "Other tetanus includes other forms of tetanus not specified elsewhere, such as localized tetanus or generalized tetanus.",
        
        "A36": "Diphtheria is a serious bacterial infection caused by Corynebacterium diphtheriae, leading to respiratory distress, heart problems, and systemic complications.",
        "A36.0": "Diphtheria, unspecified refers to cases where specific clinical details of the infection are not documented.",
        "A36.1": "Respiratory diphtheria indicates infection primarily affecting the respiratory tract, leading to sore throat, fever, and characteristic membrane formation.",
        "A36.2": "Cutaneous diphtheria refers to diphtheria infections affecting the skin, typically presenting as ulcers or lesions.",
        
        "A37": "Whooping cough, or pertussis, is a highly contagious respiratory disease caused by Bordetella pertussis, characterized by severe coughing fits.",
        "A37.0": "Whooping cough, unspecified refers to cases where the specific details of the pertussis infection are not documented.",
        "A37.1": "Whooping cough due to Bordetella pertussis indicates cases confirmed by laboratory testing or clinical diagnosis.",
        "A37.9": "Whooping cough, unspecified refers to cases where the details regarding the clinical presentation are not provided.",
        
        "A38": "Scarlet fever is a bacterial illness caused by group A Streptococcus, marked by a characteristic rash and high fever, often following strep throat.",
        "A38.0": "Scarlet fever, unspecified indicates cases without specific details on the presentation or severity.",
        
        "A39": "Meningococcal infection is caused by Neisseria meningitidis and can lead to meningitis and septicemia, characterized by sudden onset and severe symptoms.",
        "A39.0": "Meningococcal meningitis indicates inflammation of the protective membranes covering the brain and spinal cord due to meningococcal infection.",
        "A39.1": "Meningococcal septicemia refers to the presence of Neisseria meningitidis in the bloodstream, leading to systemic illness.",
        "A39.9": "Meningococcal infection, unspecified indicates cases of meningococcal disease where specific details are not documented.",
        
        "A40": "Streptococcal sepsis is a severe infection caused by group A or B Streptococcus, leading to systemic symptoms and requiring urgent medical attention.",
        "A40.0": "Streptococcal sepsis due to group A Streptococcus indicates infection from this specific bacterial group, often associated with skin and soft tissue infections.",
        "A40.1": "Streptococcal sepsis due to group B Streptococcus is commonly seen in newborns and pregnant women, requiring specific management.",
        "A40.2": "Streptococcal sepsis due to other specified Streptococcus indicates sepsis caused by other group strains not classified elsewhere.",
        
        "A41": "Other sepsis refers to systemic infections caused by various organisms that do not fall under specified categories.",
        "A41.0": "Sepsis due to Escherichia coli indicates systemic infection caused by E. coli, often linked to urinary tract infections.",
        "A41.1": "Sepsis due to Staphylococcus aureus refers to systemic infection resulting from this bacterium, often associated with skin infections.",
        "A41.9": "Sepsis, unspecified indicates cases where the specific cause or organism is not documented.",
        
        "A42": "Actinomycosis is a chronic bacterial infection caused by Actinomyces species, commonly affecting the face and neck, presenting with painful lumps.",
        "A42.0": "Actinomycosis, unspecified refers to cases where specific details of the infection are not documented.",
        "A42.1": "Cervicofacial actinomycosis indicates the presence of Actinomyces infection in the facial or neck regions.",
        "A42.9": "Other actinomycosis specifies cases that do not fit the primary classifications.",
        
        "A43": "Nocardiosis is an infection caused by Nocardia species, leading to pulmonary disease and other systemic infections, especially in immunocompromised patients.",
        "A43.0": "Nocardiosis, unspecified refers to cases where specific details of the infection are not documented.",
        "A43.1": "Pulmonary nocardiosis indicates infection affecting the lungs, often presenting with cough and fever.",
        "A43.9": "Nocardiosis, unspecified indicates cases where the details of infection are not clearly defined.",
        
        "A44": "Other bacterial diseases includes infections caused by bacteria that are not classified in specific categories.",
        "A44.0": "Other bacterial diseases, unspecified indicates cases without specific details.",
        
        "A45": "Brucellosis is a bacterial infection caused by Brucella species, primarily transmitted through unpasteurized dairy products, leading to fever and fatigue.",
        "A45.0": "Brucellosis, unspecified refers to cases where specific details of the infection are not documented.",
        
        "A46": "Erysipelas is a bacterial skin infection characterized by a raised, red rash, typically caused by Streptococcus bacteria, and often requires antibiotic treatment.",
        "A46.0": "Erysipelas, unspecified indicates cases where specific details of the infection are not documented.",
        
        "A47": "Other bacterial infections indicates infections caused by bacteria not classified elsewhere.",
        "A47.0": "Other bacterial infections, unspecified refers to cases without specific details.",
        
        "A48": "Other bacterial infections refer to infections caused by various bacteria not specified elsewhere.",
        "A48.0": "Other bacterial infections, unspecified indicates cases without specific details.",
        

        
        "A49": "Unspecified bacterial infection indicates an infection caused by bacteria where the specific type or location of the infection is not detailed.",
        "A50": "Congenital syphilis is a syphilis infection present at birth, which can cause serious health issues in newborns.",
        "A50.0": "Congenital syphilis, early refers to cases where symptoms appear in the first two years of life.",
        "A50.1": "Congenital syphilis, late refers to cases where symptoms appear after two years of life.",
        "A50.9": "Congenital syphilis, unspecified indicates congenital syphilis without specific symptoms or classification.",
        
        "A51": "Primary syphilis refers to the first stage of syphilis infection characterized by the appearance of a single sore, known as a chancre.",
        "A51.0": "Primary syphilis, unspecified indicates cases where the specific details of the primary syphilis infection are not documented.",
        "A51.1": "Primary syphilis, in pregnant women refers to the infection occurring during pregnancy, which can affect fetal health.",
        
        "A52": "Secondary syphilis is characterized by systemic symptoms such as rashes, mucous membrane lesions, and flu-like symptoms.",
        "A52.0": "Secondary syphilis, unspecified refers to cases where the specific details of the secondary syphilis infection are not documented.",
        "A52.1": "Secondary syphilis, in pregnant women indicates the infection during pregnancy, which can impact fetal development.",
        
        "A53": "Latent syphilis occurs when the infection is present without visible symptoms.",
        "A53.0": "Latent syphilis, unspecified refers to cases without documented symptoms or details.",
        "A53.1": "Latent syphilis, in pregnant women indicates the presence of latent syphilis during pregnancy.",
        
        "A54": "Tertiary syphilis refers to the late stages of syphilis that can cause severe damage to organs such as the heart and brain.",
        "A54.0": "Tertiary syphilis, unspecified indicates cases where the specific details of the tertiary syphilis infection are not documented.",
        "A54.1": "Tertiary syphilis, in pregnant women refers to tertiary syphilis diagnosed during pregnancy.",
        
        "A55": "Neurological syphilis affects the nervous system, potentially leading to various neurological issues.",
        "A55.0": "Neurological syphilis, unspecified indicates cases of neurological syphilis without specific details.",
        
        "A56": "Chlamydia infections are sexually transmitted infections caused by Chlamydia trachomatis, potentially leading to serious reproductive health issues.",
        "A56.0": "Chlamydia infection of cervix uteri refers to an infection located in the cervix.",
        "A56.1": "Chlamydia infection of rectum refers to an infection affecting the rectal area.",
        "A56.2": "Chlamydia infection of oropharynx indicates an infection in the throat area.",
        "A56.3": "Chlamydia infection of urethra refers to an infection located in the urethra.",
        "A56.4": "Chlamydia infection of eye indicates an infection affecting the eye, potentially causing conjunctivitis.",
        "A56.5": "Chlamydia infection of other sites refers to infections caused by chlamydia in locations not specified.",
        
        "A57": "Trichomoniasis is a sexually transmitted infection caused by the protozoan parasite Trichomonas vaginalis.",
        "A57.0": "Trichomoniasis, unspecified indicates cases of trichomoniasis without specific details.",
        
        "A58": "Other protozoal infections refer to infections caused by protozoa not classified elsewhere.",
        "A58.0": "Other protozoal infections, unspecified refers to cases without specific details.",
        
        "A59": "Infection by an unspecified virus indicates a viral infection where the specific virus is not identified.",
        "A59.0": "Infection by an unspecified virus refers to cases without specific details.",
        
        "A60": "Anogenital herpesviral infection refers to herpes infections in the anogenital region.",
        "A60.0": "Anogenital herpesviral infection, unspecified indicates cases without specific details.",
        "A60.1": "Herpesviral infection of vulva refers to infections affecting the vulvar area.",
        "A60.2": "Herpesviral infection of vagina indicates infections affecting the vaginal area.",
        "A60.3": "Herpesviral infection of penis refers to infections affecting the penile area.",
        
        "A61": "Human papillomavirus (HPV) infections can lead to genital warts and increase the risk of certain cancers.",
        "A61.0": "HPV infection, unspecified refers to cases without specific details.",
        
        "A62": "Infection by other specified virus indicates viral infections that are specified but not classified elsewhere.",
        "A62.0": "Infection by other specified virus, unspecified indicates cases without specific details.",
        
        "A63": "Other specified infections refers to infections that are documented but do not fit into other categories.",
        "A63.0": "Other specified infections indicates cases that have been identified but lack specific classification.",
        
        "A64": "Unspecified infection refers to infections where the causative agent is unknown or not documented.",
        "A64.0": "Unspecified infection indicates cases without specific details.",
        
        "A65": "Other diseases due to chlamydiae indicate infections caused by chlamydial organisms that do not fit into other classifications.",
        "A65.0": "Other diseases due to chlamydiae, unspecified refers to cases without specific details.",
        
        "A66": "Other diseases due to other specified organisms refers to infections caused by organisms not classified elsewhere.",
        "A66.0": "Other diseases due to other specified organisms, unspecified indicates cases without specific details.",
        
        "A67": "Infection due to other organisms refers to cases of infection caused by unspecified organisms.",
        "A67.0": "Infection due to other organisms, unspecified indicates cases without specific details.",
        
        "A68": "Infections of unspecified organisms refer to cases where the specific organism causing the infection is not identified.",
        "A68.0": "Infections of unspecified organisms, unspecified indicates cases without specific details.",
        
        "A69": "Other diseases due to zoonotic organisms indicate infections transmitted from animals to humans.",
        "A69.0": "Other diseases due to zoonotic organisms, unspecified refers to cases without specific details.",
        
        "A70": "Mycoplasma infections refer to infections caused by mycoplasmas, which can affect various body systems.",
        "A70.0": "Mycoplasma pneumonia, unspecified indicates cases of pneumonia caused by mycoplasma without specific details.",
        "A70.1": "Mycoplasma genitalium infection refers to infections caused by the Mycoplasma genitalium organism, often sexually transmitted.",
        
        "A71": "Coxiella burnetii infection refers to infections caused by the Coxiella burnetii organism, which can lead to Q fever.",
        "A71.0": "Coxiella burnetii infection, unspecified indicates cases without specific details.",
        
        "A72": "Chlamydia psittaci infection refers to infections caused by Chlamydia psittaci, primarily associated with birds.",
        "A72.0": "Chlamydia psittaci infection, unspecified indicates cases without specific details.",
        
        "A73": "Bacterial infections of the eye refer to infections affecting the ocular system caused by various bacteria, potentially leading to conjunctivitis or more severe conditions.",
        "A73.0": "Bacterial conjunctivitis indicates inflammation of the conjunctiva due to bacterial infection.",
        
        "A74": "Other bacterial infections of the respiratory system refers to respiratory infections caused by bacteria not classified elsewhere.",
        "A74.0": "Other bacterial infections of the respiratory system, unspecified indicates cases without specific details.",
        
        "A75": "Other bacterial infections indicate infections caused by various bacteria that do not fit into specific categories.",
        "A75.0": "Other bacterial infections, unspecified refers to cases without specific details.",
        
        "A76": "Bacterial infections of the gastrointestinal tract refer to infections affecting the digestive system caused by bacteria.",
        "A76.0": "Bacterial infections of the gastrointestinal tract, unspecified indicates cases without specific details.",
        
        "A77": "Bacterial infections of the skin refer to infections affecting the skin caused by various bacteria.",
        "A77.0": "Bacterial infections of the skin, unspecified indicates cases without specific details.",
        
        "A78": "Bacterial infections of the musculoskeletal system refer to infections affecting the bones and muscles caused by various bacteria.",
        "A78.0": "Bacterial infections of the musculoskeletal system, unspecified indicates cases without specific details.",
        
        "A79": "Other bacterial infections refer to infections caused by various bacteria not specified elsewhere.",
        "A79.0": "Other bacterial infections, unspecified indicates cases without specific details.",
        
        "A80": "Viral infections of the nervous system refer to infections affecting the central nervous system caused by various viruses.",
        "A80.0": "Viral infections of the nervous system, unspecified indicates cases without specific details.",
        
        "A81": "Viral infections of the respiratory system refer to infections caused by viruses affecting the respiratory tract.",
        "A81.0": "Viral infections of the respiratory system, unspecified indicates cases without specific details.",
        
        "A82": "Viral infections of the gastrointestinal tract refer to infections caused by viruses affecting the digestive system.",
        "A82.0": "Viral infections of the gastrointestinal tract, unspecified indicates cases without specific details.",
        
        "A83": "Viral infections of the skin refer to infections caused by viruses affecting the skin.",
        "A83.0": "Viral infections of the skin, unspecified indicates cases without specific details.",
        
        "A84": "Other viral infections indicate infections caused by viruses not specified elsewhere.",
        "A84.0": "Other viral infections, unspecified indicates cases without specific details.",
        
        "A85": "Unspecified viral infections indicate cases where the specific viral cause of the infection is not identified.",
        "A85.0": "Unspecified viral infections refer to cases without specific details.",
        
        "A86": "Fungal infections of the skin refer to infections caused by fungi affecting the skin.",
        "A86.0": "Fungal infections of the skin, unspecified indicates cases without specific details.",
        
        "A87": "Fungal infections of the respiratory system refer to infections caused by fungi affecting the respiratory tract.",
        "A87.0": "Fungal infections of the respiratory system, unspecified indicates cases without specific details.",
        
        "A88": "Fungal infections of the gastrointestinal tract refer to infections caused by fungi affecting the digestive system.",
        "A88.0": "Fungal infections of the gastrointestinal tract, unspecified indicates cases without specific details.",
        
        "A89": "Fungal infections of other sites refer to infections caused by fungi in areas not specified.",
        "A89.0": "Fungal infections of other sites, unspecified indicates cases without specific details.",
        
        "A90": "Other infectious diseases refer to infections caused by various pathogens that do not fit into specific classifications.",
        "A90.0": "Other infectious diseases, unspecified indicates cases without specific details.",
        
        "A91": "Infections of unknown etiology refer to cases where the causative organism of the infection is not identified.",
        "A91.0": "Infections of unknown etiology, unspecified indicates cases without specific details.",
        
        "A92": "Bacterial infections, unspecified refers to infections caused by bacteria without specific details or identification.",
        "A92.0": "Bacterial infections, unspecified indicates cases without specific details.",
        
        "A93": "Other specified infections refer to infections that are documented but do not fit into specific categories.",
        "A93.0": "Other specified infections, unspecified indicates cases without specific details.",
        
        "A94": "Unspecified infections refer to infections where the causative agent is unknown or not documented.",
        "A94.0": "Unspecified infections indicate cases without specific details.",
        
        "A95": "Yellow fever is a viral disease transmitted by mosquitoes, particularly the Aedes species. It is characterized by fever, chills, loss of appetite, and muscle pain, and can progress to severe liver damage and bleeding.",
        "A95.0": "Yellow fever, unspecified refers to cases of yellow fever where specific details regarding the severity or symptoms are not documented.",
        
        "A96": "Viral hemorrhagic fevers, not elsewhere classified refers to severe illnesses caused by various viruses that lead to hemorrhagic symptoms and significant mortality rates.",
        "A96.0": "Viral hemorrhagic fever, unspecified indicates cases where the specific viral cause or symptoms are not clearly defined, requiring supportive care.",
        
        "A97": "Viral hepatitis refers to liver inflammation caused by different viruses, including hepatitis A, B, C, D, and E, which can lead to jaundice, abdominal pain, and liver dysfunction.",
        "A97.0": "Viral hepatitis A is an acute liver infection caused by the hepatitis A virus, often transmitted through contaminated food and water.",
        "A97.1": "Viral hepatitis B is a serious liver infection caused by the hepatitis B virus, primarily transmitted through blood or sexual contact.",
        "A97.2": "Viral hepatitis C is a liver infection caused by the hepatitis C virus, often leading to chronic liver disease and transmitted through blood.",
        "A97.3": "Viral hepatitis D occurs only in those infected with hepatitis B and can worsen liver disease.",
        "A97.4": "Viral hepatitis E is an acute liver infection caused by the hepatitis E virus, often associated with contaminated water supplies.",
        "A97.9": "Viral hepatitis, unspecified refers to cases of hepatitis where the specific viral etiology or severity is not documented.",
        
        "A98": "Other viral diseases refer to a group of viral infections that do not fit into specific categories, potentially involving various body systems.",
        "A98.0": "Infection by an unspecified virus indicates cases of viral infection without specific details on the type of virus or symptoms.",
        "A98.1": "Viral infection of the skin refers to viral infections that cause skin lesions, rashes, or other dermatological issues.",
        "A98.9": "Other viral diseases, unspecified indicates cases of viral infections with no further specified details or classification.",
        
        "A99": "Unspecified infectious disease indicates cases where the specific type or cause of the infectious disease is not identified, making treatment challenging.",
        "A99.0": "Infectious disease, unspecified refers to cases of infection where the specific causative agent, symptoms, or site of infection are not documented."
    }
    
    return detailed_info.get(code, "No detailed information available for this code.")



# Function to get disease based on code
def get_disease_from_code(code):
    for block, block_info in icd_10_chapter_1.items():
        for category_code, category_info in block_info["categories"].items():
            if category_code == code or code in category_info["subcategories"]:
                detailed_info = provide_detailed_info(code)
                return {
                    "block": block,
                    "block_description": block_info["block_description"],
                    "category": category_code,
                    "category_description": category_info["description"],
                    "subcategory": category_info["subcategories"].get(code, "No subcategory found"),
                    "detailed_info": detailed_info  # Include detailed information here
                }
    return None

# Function to get code based on disease name
def get_code_from_disease(disease):
    results = []
    for block, block_info in icd_10_chapter_1.items():
        for category_code, category_info in block_info["categories"].items():
            if disease.lower() in category_info["description"].lower():
                results.append({
                    "block": block,
                    "block_description": block_info["block_description"],
                    "category": category_code,
                    "category_description": category_info["description"],
                })
            for sub_code, sub_description in category_info["subcategories"].items():
                if disease.lower() in sub_description.lower():
                    results.append({
                        "block": block,
                        "block_description": block_info["block_description"],
                        "category": sub_code,
                        "category_description": sub_description,
                    })
    return results

# Sidebar for input type
input_type = st.sidebar.selectbox(
    'Search by:',
    ['ICD-10 Code', 'Disease Name']
)

# Input form
if input_type == 'ICD-10 Code':
    icd_code_input = st.text_input('Enter ICD-10 Code (e.g., A01.0):')
    
    if icd_code_input:
        result = get_disease_from_code(icd_code_input.upper())
        if result:
            st.write(f"**Block**: {result['block']} - {result['block_description']}")
            st.write(f"**Category**: {result['category']} - {result['category_description']}")
            st.write(f"**Subcategory**: {result['subcategory']}")
            st.write(f"**Detailed Information**: {result['detailed_info']}")
        else:
            st.error("No matching disease found for this code.")

elif input_type == 'Disease Name':
    disease_input = st.text_input('Enter Disease Name (e.g., Cholera):')

    if disease_input:
        results = get_code_from_disease(disease_input)
        if results:
            for result in results:
                st.write(f"**Block**: {result['block']} - {result['block_description']}")
                st.write(f"**Category**: {result['category']} - {result['category_description']}")
                st.write("---")
        else:
            st.error("No matching ICD-10 code found for this disease.")

# Footer
st.markdown("**ICD-10 HealthInfo System** © 2024")
