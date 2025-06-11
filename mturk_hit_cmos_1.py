
def generate_classifier_block(sample_num, transcript):
    sample_id = f"sample_{sample_num:03d}"
    audio_a_url = f"https://rlataewoo.github.io/eval_sample/samples/table_2/gigaspeech_mp3/{sample_id}_A.mp3?raw=true"
    audio_b_url = f"https://rlataewoo.github.io/eval_sample/samples/table_2/gigaspeech_mp3/{sample_id}_B.mp3?raw=true"
    audio_ref_url = f"https://rlataewoo.github.io/eval_sample/samples/table_2/gigaspeech_mp3/{sample_id}_Ref.mp3?raw=true"

    return f"""
    <crowd-classifier 
        categories="['-3 Reference Much Better', '-2 Reference Better', '-1 Reference Little Better' ,'0 Equally Natural', '+1 Sample Little Better', '+2 Sample Better', '+3 Sample Much Better']"
        header="How natural does the audio sound compared to the reference? Please focus on whether the transition between the original and synthesized parts is smooth and human-like."
        name="{sample_id}-naturalness">
            <classification-target>               
                <div style="margin-bottom: 20px;">
                <label>Reference audio</label>
                <audio controls style="width: 100%">
                    <source src="{audio_ref_url}" type="audio/mp3" />
                </audio>
                </div>
         
                <div style="margin-bottom: 20px;">
                <label>Sample audio</label>
                <audio controls style="width: 100%">
                    <source src="{audio_a_url}" type="audio/mp3" />
                </audio>
                </div>
                
                <div class="sample-number" style="margin-top: 10px; margin-bottom: 10px; font-weight: bold; font-size: 30px;">Sample {sample_num:03d}-A</div>
                <div id="text_area">
                    <h3>Transcripts (edited parts are shown in <span style='color: red;'>red</span>)</h3>
                    <p>{transcript}</p>
                </div>
            </classification-target>
        <short-instructions>  
            <p>
              Listen to the sample of computer generated speech and assess the quality 
              of the audio based on how close it is to natural speech. The words in the audio are shown in the Original utterance below.
            </p>
            For better results, wear headphones and work in a quiet environment.
            If the audio file is not playing, please be patient as it may take some time for the audio file to upload.
        </short-instructions>
    </crowd-classifier>

    <crowd-classifier 
        categories="['-3 Reference Much Better', '-2 Reference Better', '-1 Reference Little Better' ,'0 Equally Natural', '+1 Sample Little Better', '+2 Sample Better', '+3 Sample Much Better']"
        header="How natural does the audio sound compared to the reference? Please focus on whether the transition between the original and synthesized parts is smooth and human-like."
        name="{sample_id}-naturalness">
            <classification-target>               
                <div style="margin-bottom: 20px;">
                <label>Reference audio</label>
                <audio controls style="width: 100%">
                    <source src="{audio_ref_url}" type="audio/mp3" />
                </audio>
                </div>
         
                <div style="margin-bottom: 20px;">
                <label>Sample audio</label>
                <audio controls style="width: 100%">
                    <source src="{audio_b_url}" type="audio/mp3" />
                </audio>
                </div>
                
                <div class="sample-number" style="margin-top: 10px; margin-bottom: 10px; font-weight: bold; font-size: 30px;">Sample {sample_num:03d}-B</div>
                <div id="text_area">
                    <h3>Transcripts (edited parts are shown in <span style='color: red;'>red</span>)</h3>
                    <p>{transcript}</p>
                </div>
            </classification-target>
        <short-instructions>  
            <p>
              Listen to the sample of computer generated speech and assess the quality 
              of the audio based on how close it is to natural speech. The words in the audio are shown in the Original utterance below.
            </p>
            For better results, wear headphones and work in a quiet environment.
            If the audio file is not playing, please be patient as it may take some time for the audio file to upload.
        </short-instructions>
    </crowd-classifier>

    """

def generate_hit_file(filename, start_idx, end_idx, transcript_map):
    html_blocks = ['<!-- You must include this JavaScript file -->',
                   '<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>',
                   '<crowd-form answer-format="flatten-objects">']
    
    for i in range(start_idx, end_idx + 1):
        transcript = transcript_map[i]
        html_blocks.append(generate_classifier_block(i, transcript))

    html_blocks.append('</crowd-form>')

    full_html = '\n'.join(html_blocks)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(full_html)


# 각 샘플 번호와 대응하는 텍스트
transcript_map = {
    1: "WE THOUGHT SIGNIFICANTLY <span style='color: red;'>ABOUT BUYING THE IRVINE CORPORATION</span> WHEN IT BECAME AVAILABLE SO.",
    2: "FEW ACTORS HAVE <span style='color: red;'>MANAGED TO SIMULTANEOUSLY CULTIVATE A REPUTATION</span> AS A SERIOUS DRAMATIC ACTOR.",
    3: "WE KNOW THAT YODA LIVED TO THE RIPE OLD AGE OF NINE <span style='color: red;'>HUNDRED IN RETURN OF THE JEDI WHICH EVERYONE ELSE IS SURPRISED ABOUT BUT HE ISN'T</span> SEEMING TO INDICATE THAT IT'S NOT REALLY THAT BIG OF A DEAL FOR HIM.",
    4: "PRETTY MUCH ALL WE <span style='color: red;'>CAN TELL YOU IS THAT THIS INSTALLMENT</span> FOLLOWS THE EVENTS OF EPISODE SEVEN.",
    5: "YOU ARE GONNA HAVE AMBIENT IF YOU ARE ON <span style='color: red;'>THE BIKE YOU'RE CYCLING YOU COULD HEAR IF IF A CAR</span> HONKS ITS HORN OR SOMETHING. THIS COULD REALLY AMPLIFY YOUR SURROUNDINGS.",
    6: "HE MAY BE ON <span style='color: red;'>AIR ON SATURDAY SHE WAS GONNA</span> CO CO-STAR THE U F C.",
    7: "PRESENTING THE APOCALYPTIC ADVENTURE <span style='color: red;'>OF AN ELEVEN YEAR OLD BOY NAMED</span> JAKE CHAMBERS AS HE ACCIDENTALLY UNCOVERS.",
    8: "YEAH WHATEVER IS RIGHTS OF ANOTHER FIVE DOLLARS <span style='color: red;'>DO YOU THINK PAPA G IT IS WERE PROBABLY THREE</span> OR FOUR BUCKS AWAY FROM FROM GETTING HIM TO GO.",
    9: "EVEN THOUGH AS A TEAM WE <span style='color: red;'>HAD YOU KNOW WE WE WE WERE IN LAST</span> PLACE FOR ME IT WASN'T A BAD CUT.",
    10: "IT ALSO ENSURES FOR THE FIRST TIME <span style='color: red;'>THAT THE LAWS CANNOT TREAT PEOPLE DIFFERENTLY BASED ON</span> THEIR RACE. THIS IS CALLED THE EQUAL PROTECTION CLAUSE.",

    11: "BUT THEN I'M ALWAYS AT HOME. <span style='color: red;'>ONE BOGGY PLACE IS MUCH LIKE ANOTHER AND</span> I DON'T HOLD WITH ALL THIS PACKING UP.",
    12: "A BONUS CHECK THIRD <span style='color: red;'>IN TEN FLIES OVER HIS HEAD AND</span> FALL ON ON IT BUT THIRTY-FOUR.",
    13: "FROM THEIR LESSER KNOWN ORIGINS IN THAILAND TO THEIR <span style='color: red;'>RISE AS A GLOBAL MARKETING EMPIRE. IF YOU'D LIKE TO WATCH</span> THE FULL BEHIND THE BUSINESS SERIES YOU CAN CLICK HERE.",
    14: "WE JUST HIT NEXT WE GO THROUGH WE CREATE AN <span style='color: red;'>AD I UNDERSTAND I AM PAYING FOR MY OWN AD SPEND THEN WE</span> COME OVER HERE TARGET CITY WE'LL SAY WE ARE GOING FOR PHOENIX.",
    15: "I WOULD ALSO TAKE WHATEVER IS <span style='color: red;'>LEFT BECAUSE SOMETHING IS BETTER THAN NOTHING FOR PEOPLE</span> WHO ARE STRUGGLING EVEN THOUGH IT'S NOT MUCH.",
    16: "LIKE I REALLY <span style='color: red;'>DON'T GET ANNOYED WITH MIKE CAUSE</span> HE HAS CHARACTER AND INTEGRITY.",
    17: "YOU MAY THINK THAT YOU HAVE A RATIONAL <span style='color: red;'>JUSTIFICATION FOR EVERY VIEW THAT YOU HOLD. YOU MAY THINK</span> IT'S THE GREATEST WORLDVIEW THAT IT'S EVER BEEN CREATED.",
    18: "YOU ARE A RESIDENT OF NEW YORK STATE <span style='color: red;'>THERE IS A SEAT THAT IS OPEN AND YOU HAVE</span> THE ABILITY TO TAKE THAT SEAT IN MANY PEOPLE'S OPINION.",
    19: "SO LET'S TAKE THAT LINK AND <span style='color: red;'>JUMP INTO OUR FACEBOOK. HERE I AM INSIDE</span> OF MY FACEBOOK PAGE FOR COREY ASH.",
    20: "I DID GIVE UP <span style='color: red;'>BUT I SHOULDN'T HAVE. I I MUST</span> KEEP TRYING AND YOU SHOULD TOO.",

    21: "WHERE DO WE WANNA SEND THEM? SO OVER HERE GUYS <span style='color: red;'>WE HAVE YOUR FACEBOOK PAGE YOU CAN HAVE THEM GO TO YOUR</span> WEBSITE YOU CAN HAVE THEM BOOK AN APPOINTMENT WITH YOU OR.",
    22: "THE EUROPEAN IN AFRICA IS <span style='color: red;'>AN EXPAT AND THE AFRICAN IN EUROPEAN IS</span> A MIGRANT. IT CAN'T CONTINUE LIKE THAT.",
    23: "AND STUDIES HAVE SHOWN THAT WHEN WE GIVE <span style='color: red;'>IT TRIGGERS THE SAME CHEMICAL REACTIONS IN OUR BRAINS IS FALLING</span> IN LOVE OR BONDING WITH A NEWBORN CHILD.",
    24: "A DISEASE IS <span style='color: red;'>NOT GONNA IF YOU LOOK</span> AT THE NUMBERS AT YOUTA.",
    25: "REMEMBER HOW EARLIER I SAID THESE NEURONS ARE <span style='color: red;'>SIMPLY THINGS THAT HOLD NUMBERS WELL OF COURSE THE SPECIFIC NUMBERS</span> THAT THEY HOLD DEPENDS ON THE IMAGE YOU FEED IN.",
    26: "WHAT'S INTERESTING IS THAT YOU WROTE IT <span style='color: red;'>TOGETHER. YOU'VE WRITTEN MANY BOOKS SEPARATELY BUT THIS WAS</span> YOUR FIRST BOOK WRITING TOGETHER AS MOTHER AND DAUGHTER.",
    27: "AND YEAH WE WE ENDED UP <span style='color: red;'>IN THE SAME SPOT SO THERE'D BE LESSON</span> KIDS IS TO AH NOT BE RESPONSIBLE.",
    28: "THIS IS JUST SO <span style='color: red;'>COZY UP HERE. AND HAVING THAT</span> SKYLIGHT IS JUST LOVELY ISN'T IT.",
    29: "YES YES OKAY SO I'LL PUT A LINK <span style='color: red;'>TO ALL THAT STUFF IN THE SHOW NOTES FOR YOU</span> GUYS AS WELL AS KATIE'S AWESOME OF THE WEEK.",
    30: "WHEN YOU'RE MAKING DECISIONS THAT'S A GOOD THAT'S A TRAIT OF <span style='color: red;'>A GOOD HUMAN BEING TO DO THAT BY THE WAY IT DOESN'T DOESN'T</span> MAKE YOU WEAK TO CONSIDER THE FEELINGS AND PLIGHT OF OTHER PEOPLE.",

    31: "WITH TWO COLLEAGUES <span style='color: red;'>I WORKED UM SORT OF BUILDING</span> A DISTRIBUTION AND WE WE.",
    32: "AND THERE ISN'T JUST <span style='color: red;'>ONE DELIVERY THAT HAPPENS AT THE</span> BEGINNING OF A SEASON. NO NO.",
    33: "WELL THE DIFFICULTIES THEY HAVE IS COMMUNICATING WITH YOUNG PEOPLE BECAUSE <span style='color: red;'>CONSERVATIVES WHAT WHAT THE HELL ARE THEY GONNA SELL TO YOUNG PEOPLE RIGHT CAUSE</span> BEING CONSERVATIVE IS SOMETHING THAT HAPPENS WHEN YOU'RE OLDER.",
    34: "AT THE END OF THIS COURSE <span style='color: red;'>YOU WILL BE ABLE TO EXPLAIN THE THREE FUNDAMENTAL</span> CHARACTERISTIC THAT DEFINE THE BLOCKCHAIN USING BITCOIN BLOCKCHAIN.",
    35: "YOU GET THE TRASH OUT IF <span style='color: red;'>I GET STEVE COME OVER HERE PUT HIS</span> DAMN HANDS ON YOU AGAIN OH OH.",
    36: "AND IT'S AVAILABLE FOR BOTH MAC AND WINDOWS <span style='color: red;'>DOES CAUSE NINETEEN DOLLARS NINETY-NINE FOR THE YEAR FOR A</span> SUBSCRIPTION TO THIS SOFTWARE BUT IT IS SO MUCH MORE.",
    37: "CLAUDE MONET'S WATER LILIES SERIES <span style='color: red;'>WAS PAINTED AT HIS HOME IN GIVERNY</span> BETWEEN EIGHTEEN NINETY-SIX AND NINETEEN TWENTY-SIX.",
    38: "I DIDN'T REALIZE THAT <span style='color: red;'>WAS MATH. OH IF THAT'S MATH</span> THEN I COULD DO THAT.",
    39: "BECAUSE <span style='color: red;'>FAST FASHION HAS AS</span> ITS FUNDAMENTAL PURPOSE.",
    40: "ROEMER SUPPORTERS WERE NOW <span style='color: red;'>UP FOR GRABS IF THEY VOTED</span> REPUBLICAN IN THE NOVEMBER RUNOFF.",
}

generate_hit_file("hit_cmos_1.html", 1, 40, transcript_map)
