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
    
# Function to get disease based on code
def get_disease_from_code(code):
    for block, block_info in icd_10_chapter_1.items():
        for category_code, category_info in block_info["categories"].items():
            if category_code == code or code in category_info["subcategories"]:
                return {
                    "block": block,
                    "block_description": block_info["block_description"],
                    "category": category_code,
                    "category_description": category_info["description"],
                    "subcategories": category_info["subcategories"].get(code, "No subcategory found"),
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
            st.write(f"**Subcategory**: {result['subcategories']}")
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
